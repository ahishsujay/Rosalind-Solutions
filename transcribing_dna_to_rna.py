def Transcribe(dna):
    rna = ""
    for i in dna:
        if i == "A" or i == "G" or i == "C":
            rna = rna + i
        if i == "T":
            rna = rna + "U"
    print(rna)
