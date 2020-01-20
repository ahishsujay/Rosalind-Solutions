def CountNucleotides(s):
    dna_nucl = {"A":0,"C":0,"G":0,"T":0}
    for nucl in s:
        if nucl == "A":
            dna_nucl[nucl] += 1
        if nucl == "C":
            dna_nucl[nucl] += 1
        if nucl == "G":
            dna_nucl[nucl] += 1
        if nucl == "T":
            dna_nucl[nucl] += 1

    print(dna_nucl["A"],dna_nucl["C"],dna_nucl["G"],dna_nucl["T"])
