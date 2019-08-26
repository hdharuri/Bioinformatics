import re
from collections import Counter

filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_gc.txt"

sequences = {}

start = True
seq = ''
with open(filepath, 'r') as f:
    while True:
        line = f.readline()
        if re.match(">", line):
            if start:
                start = False
                identifier = line.rstrip()
            else:
                sequences[identifier] = seq
                # reset the identifier and the seq
                identifier = line.rstrip()
                seq = ''
        else:
            if len(line.rstrip()) == 0:
                sequences[identifier] = seq
                break
            seq = seq + line.rstrip()

gc_percent_dict = {}
for item in sequences:
    counter = dict(Counter(sequences[item]))
    sum_total = sum(counter.values())
    gc = 0
    for base in counter:
        if base == 'G' or base == 'C':
            gc += counter[base]
    gc_percent = (gc / float(sum_total)) * 100
    # insert into the dictionary
    gc_percent_dict[item] = gc_percent

sorted_gc_percent = sorted(gc_percent_dict.items(), key = lambda t: t[1], reverse = True)

# print the identifier that has the maximum gc percent
print(sorted_gc_percent)
print(sorted_gc_percent[0][0])
print(round(sorted_gc_percent[0][1],6))
