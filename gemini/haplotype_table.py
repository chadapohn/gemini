class haplotype:

    def __init__(self, col):
        col = [None if c == 'None' else c for c in col]
        self.cols = col[:]
        self.gene_symbol = col[0]
        self.name = col[1]
        self.num_variants = col[2]

    def __str__(self):
        return ",".join([self.gene_symbol, self.name, self.num_variants])