import random
import numpy as np

filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_iprb.txt"
p = []
dominant_allele_probability = []

with open(filepath, 'r') as f:
    line = f.readline()
    line.rstrip()
    pop_zygosity_list = line.split()
    dominant =   ["homo_d"] * int(pop_zygosity_list[0])
    hetero =   ["hetero"] * int(pop_zygosity_list[1])
    recessive =   ["homo_r"] * int(pop_zygosity_list[2])
    p.append(dominant)
    p.append(hetero)
    p.append(recessive)
    p = [item for sublist in p for item in sublist]

# probability of a dominant allele being present in the offspring if the parents are:
d_r = ['homo_d', 'homo_r']
h_r = ['hetero', 'homo_r']
d_d = ['homo_d', 'homo_d']
r_r = ['homo_r', 'homo_r']
h_h = ['hetero', 'hetero']
d_h = ['hetero', 'homo_d']

for i in range(10000000):
    s = sorted(random.sample(p,2))
    if s == d_r:
        dominant_allele_probability.append(1)
    elif s == h_r:
        dominant_allele_probability.append(0.5)
    elif s == d_h:
        dominant_allele_probability.append(1)
    elif s == d_d:
        dominant_allele_probability.append(1)
    elif s == h_h:
        dominant_allele_probability.append(0.75)
    elif s == r_r:
        dominant_allele_probability.append(0)

print(np.mean(dominant_allele_probability))
