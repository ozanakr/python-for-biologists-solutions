# variables
header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"
seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2 = "actgatcgacgatcgatcgatcacgact"
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# open a file, then write the values into it.
output = open("sequences.fasta", "w")
output.write(">" + header1 + "\n" + seq1 + "\n")
output.write(">" + header2 + "\n" + seq2.upper() + "\n")
output.write(">" + header3 + "\n" + seq3.replace("-", "") + "\n")
