my_file = open("input.txt")
output = open("trimmed.txt", "w")
for line in my_file:
    cutted = line[14:]
    print(cutted)
    output.write(cutted)

# actual solution

"""

# open the input file
file = open("input.txt")

# open the output file
output = open("trimmed.txt", "w")

# go through the input file one line at a time
for dna in file:
    # calculate the position of the last character
    last_character_position = len(dna)
    # get the substring from the 15th character to the end
    trimmed_dna = dna[14:last_character_position]
    # print out the trimmed sequence
    output.write(trimmed_dna)
    # print out the length to the screen
    print("processed sequence with length " + str(len(trimmed_dna)))

"""