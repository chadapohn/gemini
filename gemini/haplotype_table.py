class haplotype:

    def __init__(self, col):
        col = [None if c == 'None' else c for c in col]
        self.cols = col[:]
        self.gene = col[0]
        self.chrom = col[1]
        self.name = col[2]
        self.num_variants = col[3]
        self.starts = col[4]
        self.ends = col[5]
        self.chrom_hgvs_names = col[6]
        self.rsids = col[7]
        self.alleles = col[8]
        self.types = col[9]

    def __str__(self):
        return ",".join([self.gene, self.chrom, self.name, self.num_variants,
                        self.starts, self.ends, self.chrom_hgvs_names,
                        self.rsids, self.alleles, self.types])

class  haplotype_allele:
    def __init__(self, col):
        col = [None if c == 'None' else c for c in col]
        self.cols = col[:]
        self.chrom = col[0]
        self.start = col[1]
        self.end = col[2]
        self.chrom_hgvs_name = col[3]
        self.rsid = col[4]
        self.allele = col[5]
        self._iupac_pattern = col[6]
        self.type = col[7]

    def __str__(self):
        return ",".join([self.chrom, self.start, self.end, str(self.chrom_hgvs_name),
                        self.rsid, self.allele, self._iupac_pattern, self.type])