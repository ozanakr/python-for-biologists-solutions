#store dna sequence in a variable
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#look for AT content
A_num = dna.count("A")
T_num = dna.count("T")
AT_cont = (A_num + T_num) / len(dna)

#print at content
print("AT content is: " + str(AT_cont))