import pysam
import re
from . import annotations

tabix_vcf = None

def load_tabix_vcf(args):
    # TODO: raise IOError if gemini can't open input vcf file
    vcf = args.vcf
    if vcf.endswith(".gz"):
        global tabix_vcf
        tabix_vcf = pysam.Tabixfile(vcf)

def match(allele):
    match_left = []
    match_right = []
    coords = get_vcf_coords(allele)
    hits = annotations._get_hits(coords, tabix_vcf, parser_type="vcf") # can be multile hit records i.e overlap positions
    for hit in hits: # variant level
        # assume a single hit
        gts_left = []
        gts_right = []
        
        start = hit.pos
        if start != coords[1]: 
            # missing variant matched_score = []
            return match_left, match_right
        
        ref, alt = annotations._get_var_ref_and_alt(hit)
        alleles = [] # [REF, ALT1, ALT2, ..]
        alleles.append(ref)
        alleles.extend(alt)

        for i in range(0, len(hit)): # sample level
            call = hit[i].split(":")[0] # "0/0"
            call_list = list(map(int, re.split(r'[|/]', call))) # i.e [0, 0]
            gt_left = alleles[call_list[0]]
            gt_right = alleles[call_list[1]]
            if allele.type == "ins":
                gt_left = convert_insertion(gt_left, ref)
                gt_right = convert_insertion(gt_right, ref)
            elif allele.type == "del":
                gt_left = convert_deletion(gt_left, ref)
                gt_right = convert_deletion(gt_right, ref)
            gts_left.append(gt_left)
            gts_right.append(gt_right)

        allele_pattern = re.compile(allele._iupac_pattern)
        for gt in gts_left:
            if allele_pattern.match(gt):
                match_left.append(1)
            else: match_left.append(0)
        for gt in gts_right:
            if allele_pattern.match(gt):
                match_right.append(1)
            else: match_right.append(0)

    return match_left, match_right

def get_vcf_coords(allele):
    chrom = allele.chrom
    start = int(allele.start)
    if allele.type == "DEL":
        allele.start=allele.start-1
    end = int(allele.end)
    return chrom, start, end

def convert_insertion(gt, ref):
    if gt == ref:
        return "del" # remove padding base 
    return "ins" + ref[1:]

def convert_deletion(gt, ref):
    if gt == ref:
        return ref[1:]
    return 'del'+ gt[1:]