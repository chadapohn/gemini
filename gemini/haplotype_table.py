from . import iupac

class haplotype:

    def __init__(self, col):
        col = [None if c == 'None' else c for c in col]
        self.cols = col[:]
        self.gene = col[0]
        self.name = col[1]
        self.num_variants = col[2]
        self.starts = col[3]
        self.ends = col[4]
        self.chrom_hgvs_names = col[5]
        self.rsids = col[6]
        self.alleles = col[7]
        self.types = col[8]

    def __str__(self):
        return ",".join([self.gene, self.name, self.num_variants,
                        self.starts, self.ends, self.chrom_hgvs_names,
                        self.rsids, self.alleles, self.types])

class  haplotype_alleles:
    def __init__(self, col):
        col = [None if c == 'None' else c for c in col]
        self.cols = col[:]
        self.start = col[0]
        self.end = col[1]
        self.chrom_hgvs_name = col[2]
        self.rsid = col[3]
        self.allele = col[4]
        self._iupac_pattern = "[" + ''.join(iupac.lookup(self.allele)) + "]"
        self.type = col[6]

    def __str__(self):
        return ",".join([self.start, self.end, str(self.chrom_hgvs_name),
                        self.rsid, self.allele, self._iupac_pattern, self.type])