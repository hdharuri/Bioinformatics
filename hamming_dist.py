import random
import numpy as np

filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_hamm.txt"

hamming_dist = 0
with open(filepath,'r') as f:
    string1 = f.readline()
    string1 = string1.rstrip()
    string2 = f.readline()
    string2 = string2.rstrip()

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            hamming_dist += 1

print(hamming_dist)
