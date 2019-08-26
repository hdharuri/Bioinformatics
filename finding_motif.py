import re

filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_subs.txt"

with open(filepath, 'r') as f:
    t = f.readline()
    t = t.rstrip()
    p = f.readline()
    p = p.rstrip()

    p_re = '(?=(' + p + '))'
    match_index = re.finditer(p_re,t)
    output = [(m.start(0) + 1) for m in match_index]
    print(output)
