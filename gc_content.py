'''
NOTE: Needs to be fixed, logic is right, but getting the sequence and header is wrong as a ">" always needs to be added to the end of the text file. Code needs to be cleaned.
'''


with open("rosalind_gc copy.txt") as fh:
    header = []
    nucl = []
    nucl_dict = {}
    test = []
    '''
    for line in fh.readlines():
        seq = ''
        if line.startswith(">"):
            line = line.strip(">")
            line = line.rstrip("\n")
            header.append(line)
            #nucl_dict[line] = None

        else:
            test.append(line)
            line = line.rstrip("\n")
            seq += line
            #print(line)
            nucl.append(line)
    '''
    key = ''
    val = ''
    for line in fh.readlines():
        if line.startswith(">"):        #If starts with >
            if val != "":               #If string val is not empty, then enter this if statement. Doesn't enter the first time as the string val is empty
                #nucl_dict[key] = val    #The key:value pair stored will get updated when it encounters the next header with ">" and as val is not empty, will execute this line of code
                header.append(key)
                nucl.append(val)
            key = line.strip(">")       #Stores the fasta header in key
            #header.append(key)
            val = ""                    #Makes val empty
        else:
            line = line.rstrip("\n")    #Once header is stored, "line" will not encounter a "-", and hence will enter this else statement. Strips the new line character for a continuous sequence
            val = val + line            #Val will keep appending the sequence and storing in variable "val"

gc = []
for i in range(0,len(nucl)):
    count = 0
    for j in range(0,len(nucl[i])):
        if nucl[i][j] == "G" or nucl[i][j] == "C":
            count += 1
    gc_content = (count/len(nucl[i]))*100
    gc.append(gc_content)

nucl_dict = dict(zip(header,gc))
#print(nucl_dict)

max = max(nucl_dict,key=nucl_dict.get)

print(max)
print(nucl_dict[max])
