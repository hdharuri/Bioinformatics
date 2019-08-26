filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_revc.txt"
dna_complement = ''
complement_dict = {'A':'T','C':'G','T':'A','G':'C'}
with open(filepath) as f:
    dna = f.readline()
    dna = dna.rstrip()
    dna.replace("\n",'')
    dna_rev = dna[::-1]
    for i in range(len(dna_rev)):
        dna_complement += complement_dict[dna_rev[i]]

fw = open("dna_revc_output.txt", "w")
fw.write(dna_complement)
fw.close()

# dna = 'AAAACCCGGT'
# #dna = list(dna)
# complement_dict = {'A':'T','C':'G','T':'A','G':'C'}
#
# dna_rev = dna[::-1]
# dna_complement = ''
# for i in range(len(dna_rev)):
#     dna_complement += complement_dict[dna_rev[i]]
#
# print(dna_rev)
# print(dna_complement)
