# variables
header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2 = "actgatcgacgatcgatcgatcacgact"
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# open multiple files, then write the values into them.
output1 = open(header1 + ".fasta", "w")
output2 = open(header2 + ".fasta", "w")
output3 = open(header3 + ".fasta", "w")

#writing the sequences
output1.write(">" + header1 + "\n" + seq1 + "\n")
output2.write(">" + header2 + "\n" + seq2.upper() + "\n")
output3.write(">" + header3 + "\n" + seq3.replace("-", "") + "\n")
