def RNAtoProtein(s):
    codon_table = {'TTT':'F',      'CTT':'L',      'ATT':'I',      'GTT':'V',
                   'TTC':'F',      'CTC':'L',      'ATC':'I',      'GTC':'V',
                   'TTA':'L',      'CTA':'L',      'ATA':'I',      'GTA':'V',
                   'TTG':'L',      'CTG':'L',      'ATG':'M',      'GTG':'V',
                   'TCT':'S',      'CCT':'P',      'ACT':'T',      'GCT':'A',
                   'TCC':'S',      'CCC':'P',      'ACC':'T',      'GCC':'A',
                   'TCA':'S',      'CCA':'P',      'ACA':'T',      'GCA':'A',
                   'TCG':'S',      'CCG':'P',      'ACG':'T',      'GCG':'A',
                   'TAT':'Y',      'CAT':'H',      'AAT':'N',      'GAT':'D',
                   'TAC':'Y',      'CAC':'H',      'AAC':'N',      'GAC':'D',
                   'TAA':'Stop',   'CAA':'Q',      'AAA':'K',      'GAA':'E',
                   'TAG':'Stop',   'CAG':'Q',      'AAG':'K',      'GAG':'E',
                   'TGT':'C',      'CGT':'R',      'AGT':'S',      'GGT':'G',
                   'TGC':'C',      'CGC':'R',      'AGC':'S',      'GGC':'G',
                   'TGA':'Stop',   'CGA':'R',      'AGA':'R',      'GGA':'G',
                   'TGG':'W',      'CGG':'R',      'AGG':'R',      'GGG':'G'}

    x = ''
    for i in range(0,len(s),3):
        if codon_table[s[i:i+3]] == "Stop":
            break
        else:
            x+= codon_table[s[i:i+3]]
    print(x)

RNAtoProtein("ATGGTTAAAGTTTATGCCCCGGCTTCCAGTGCCAATATGAGCGTCGGGTTTGATGTGCTCGGGGCGGCGGTGACACCTGTTGATGGTGCATTGCTCGGAGATGTAGTCACGGTTGAGGCGGCAGAGACATTCAGTCTCAACAACCTCGGACGCTTTGCCGATAAGCTGCCGTCAGAACCACGGGAAAATATCGTTTATCAGTGCTGGGAGCGTTTTTGCCAGGAACTGGGTAAGCAAATTCCAGTGGCGATGACCCTGGAAAAGAATATGCCGATCGGTTCGGGCTTAGGCTCCAGTGCCTGTTCGGTGGTCGCGGCGCTGATGGCGATGAATGAACACTGCGGCAAGCCGCTTAATGACACTCGTTTGCTGGCTTTGATGGGCGAGCTGGAAGGCCGTATCTCCGGCAGCATTCATTACGACAACGTGGCACCGTGTTTTCTCGGTGGTATGCAGTTGATGATCGAAGAAAACGACATCATCAGCCAGCAAGTGCCAGGGTTTGATGAGTGGCTGTGGGTGCTGGCGTATCCGGGGATTAAAGTCTCGACGGCAGAAGCCAGGGCTATTTTACCGGCGCAGTATCGCCGCCAGGATTGCATTGCGCACGGGCGACATCTGGCAGGCTTCATTCACGCCTGCTATTCCCGTCAGCCTGAGCTTGCCGCGAAGCTGATGAAAGATGTTATCGCTGAACCCTACCGTGAACGGTTACTGCCAGGCTTCCGGCAGGCGCGGCAGGCGGTCGCGGAAATCGGCGCGGTAGCGAGCGGTATCTCCGGCTCCGGCCCGACCTTGTTCGCTCTGTGTGACAAGCCGGAAACCGCCCAGCGCGTTGCCGACTGGTTGGGTAAGAACTACCTGCAAAATCAGGAAGGTTTTGTTCATATTTGCCGGCTG")
