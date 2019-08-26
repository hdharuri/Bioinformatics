

filepath = "/Users/harishdharuri/Documents/Rosalind/rosalind_rna.txt"
#dna = 'GATGGAACTTGACTACGTAAATT'
rna = ''

with open(filepath) as f:
    for dna in f:
        rna = dna.replace('T','U')
        rna = rna.strip()

fw = open("rna_output.txt", "w")
fw.write(rna)
fw.close()
