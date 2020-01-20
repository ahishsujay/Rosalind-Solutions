def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

def Reverse(Pattern):
    reverse = ""
    for i in Pattern:
        reverse = i + reverse
    return reverse

def Complement(Pattern):
    complement = ""
    for i in Pattern:
        if i == "A":
            complement = complement + "T"
        elif i == "T":
            complement = complement + "A"
        elif i == "G":
            complement = complement + "C"
        elif i == "C":
            complement = complement + "G"
    return complement
