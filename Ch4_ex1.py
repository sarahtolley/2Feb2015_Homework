#open the input file with DNA sequences
file = open("input.txt")

#create output file
output = open("trimmed_dna.txt", "w")

#create for loop
for dna in file:
	trimmed_dna = dna[14:]
	#print the trimmed dna sequence
	output.write(trimmed_dna)
	#print the length of the trimmed dna to the screen
	print("processed sequence length " + str(len(trimmed_dna)))