with open("rosalind_ini5.txt") as fh:
    line = []
    for i in fh.readlines():
        i = i.rstrip("\n")
        line.append(i)

i = 1
while i < len(line):
    print(line[i])
    i = i + 2
