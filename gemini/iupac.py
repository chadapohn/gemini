iupac = {
    "A": ["A"],
    "C": ["C"],
    "G": ["G"],
    "T": ["T"],
    "R": ["A","G"],
    "Y": ["C","T"],
    "S": ["G","C"],
    "W": ["A","T"],
    "K": ["G","T"],
    "M": ["A","C"], 
    "B": ["C","G","T"],
    "D": ["A","G","T"],
    "H": ["A","C","T"],
    "V": ["A","C","G"],
    "N": ["A","T","C","G"],
    "-": ["del"],
}

def lookup(allele):
    if allele.type == "ins" or allele.type == "del":
        return allele.allele
    return iupac[allele.allele]
