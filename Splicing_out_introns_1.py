dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
#first exon splicing
first_exon = dna[:63]
print("first exon is: " + first_exon)
print(str(len(first_exon)) + " bases")

#second exon splicing
second_exon = dna[90:]
print("second exon is: " + second_exon)
print(str(len(second_exon)) + "bases")