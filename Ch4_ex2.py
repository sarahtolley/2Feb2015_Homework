#open file, use read() to read the file all at once
genomic_dna = open("genomic_dna.txt").read()
#open exons.txt
exons = open("exons.txt")
#assign empty string
sequence = ""
#print the lines in the exons.txt file
for line in exons:
	#split each line into the start and stop position
	positions = line.split(',')
	#designate the start and stop positions
	#use int to turn strings into numbers
	start = int(positions[0])
	stop = int(positions[1])
	exon = genomic_dna[start:stop]
	sequence = sequence + exon

#write the coding sequence to an output file
output = open("coding_sequence.txt","w")
output.write(sequence)
output.close()

