
import re
filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_grph.txt"

sequences = {}
start = True
identifier = ''
seq = ''

with open(filepath, 'r') as f:
    while True:
        line = f.readline()
        line = line.rstrip()
        if re.match(">", line):
            if start:
                start = False
                identifier = line
            else:
                sequences[identifier] = seq
                #reset the identifier and the seq
                identifier = line
                seq = ''
        else:
            if len(line) == 0:
                sequences[identifier] = seq
                break
            else:
                seq = seq + line

# create a dictionary of prefixes, all possible prefixes of the sequences as keys and sequence identifiers as value_counts

all_prefixes = {}
all_suffixes = {}
for item in sequences:
    seq = sequences[item]
    prfx = seq[0:3]
    if prfx in all_prefixes:
        all_prefixes[prfx].append(item)
    else:
        identifier_lst = [item]
        all_prefixes[prfx] = identifier_lst
    # now for the suffix dictionary
    sufx = seq[-3::]
    if sufx in all_suffixes:
        all_suffixes[sufx].append(item)
    else:
        identifier_lst = [item]
        all_suffixes[sufx] = identifier_lst

# iterate through the suffixes
adjacency_list = []
for item_prfx in all_prefixes:
    for item_sufx in all_suffixes:
        if item_prfx == item_sufx:
            for i in range(len(all_prefixes[item_prfx])):
                for j in range(len(all_suffixes[item_sufx])):
                    prfx_identifier =  all_prefixes[item_prfx][i]
                    sufx_identifier = all_suffixes[item_sufx][j]
                    if prfx_identifier != sufx_identifier:
                        adjacency_tuple = (sufx_identifier,prfx_identifier)
                        adjacency_list.append(adjacency_tuple)


fw = open("overlap_graph_output.txt", "a")

for i in range(len(adjacency_list)):
    str_tuple = str(adjacency_list[i])
    str_tuple = str_tuple.replace('(','').replace(')','').replace(',','').replace('\'','').replace('>','')
    fw.write(str_tuple)
    fw.write("\n")

fw.close()
