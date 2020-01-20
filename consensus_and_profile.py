with open("test_2.txt") as fh:
    seq = []                            #"seq" list stores nucleotides characters as a matrix
    for line in fh.readlines():
        if line.startswith(">"):
            continue
        else:
            line = line.rstrip("\n")
            seq.append(list(line))      #Storing the nucleotides characters in "seq"

#Calculate counts of A,C,G and T in FASTA file
list_a = []                             #list_a stores count of A
list_c = []                             #list_c stores count of C
list_g = []                             #list_g stores count of G
list_t = []                             #list_t stores count of T
for j in range(0,len(seq[0])):
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    for i in range(0,len(seq)):
        if seq[i][j] == "A":
            count_a += 1
        if seq[i][j] == "C":
            count_c += 1
        if seq[i][j] == "G":
            count_g += 1
        if seq[i][j] == "T":
            count_t += 1

    list_a.append(count_a)
    list_c.append(count_c)
    list_g.append(count_g)
    list_t.append(count_t)

#Store counts in "matrix" to calculate consensus sequence
matrix = []
for i in range(len(list_a)):
    matrix.append([list_a[i], list_c[i], list_g[i], list_t[i]]) #matrix stores counts to calculate the consensus_sequence
consensus_sequence = ""
for i in range(len(matrix)):
    if max(matrix[i]) == matrix[i][0]:
        consensus_sequence += "A"
    if max(matrix[i]) == matrix[i][1]:
        consensus_sequence += "C"
    if max(matrix[i]) == matrix[i][2]:
        consensus_sequence += "G"
    if max(matrix[i]) == matrix[i][3]:
        consensus_sequence += "T"
print(consensus_sequence)

#"final_matrix" in order to print to std out as needed
final_matrix = list([list_a,list_c,list_g,list_t])
list_a.insert(0,"A: ")
list_c.insert(0,"C: ")
list_g.insert(0,"G: ")
list_t.insert(0,"T: ")

for row in final_matrix:
    for element in row:
        print(element, end=" ")
    print("")
