filepath = "/Users/harishdharuri/Documents/Rosalind/rosalind_dna.txt"

nucleotides = {}
with open(filepath) as f:
    for line in f:
        for nucleotide in line:
            if nucleotide in nucleotides:
                nucleotides[nucleotide] += 1
            else:
                nucleotides[nucleotide] = 1

print(nucleotides['A'])
print(nucleotides['C'])
print(nucleotides['G'])
print(nucleotides['T'])
