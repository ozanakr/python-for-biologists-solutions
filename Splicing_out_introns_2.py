dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#first exon splicing
first_exon = dna[:63]
print("first exon is: " + first_exon)
print(str(len(first_exon)) + " bases")

#second exon splicing
second_exon = dna[90:]
print("second exon is: " + second_exon)
print(str(len(second_exon)) + "bases")

#calculate the percentage of coding part of the dna
percentage = (len(first_exon) + len(second_exon))/len(dna)
print("%" + str(percentage*100) + " percentage is coding")