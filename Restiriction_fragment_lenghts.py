my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#find the fragments with .find than add 1 for the cut site
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length

print("length of fragment one is " + str(frag1_length))
print("length of fragment two is " + str(frag2_length))
print(len(my_dna))