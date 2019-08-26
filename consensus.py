import pandas as pd
import re

filepath = "/Users/harishdharuri/Documents/Rosalind/data/rosalind_cons.txt"

sequences = []
seq = ''
start = True

with open(filepath, 'r') as f:
    while True:
        line = f.readline()
        if re.match(">", line):
            if start:
                start = False
                identifier = line.rstrip()
            else:
                sequences.append(list(seq))
                seq = ''

        else:
            if len(line.rstrip()) == 0:
                sequences.append(list(seq))
                break
            seq = seq + line.rstrip()

df = pd.DataFrame(sequences)
columns = list(df)

# create a list that will hold the value_counts of each column
# this will be concatenated later along axis = 1 to create a dataframe of profiles

profile_list = []
consensus = ''
for i in columns:
    profile_list.append(df[i].value_counts())
    consensus += df[i].value_counts().idxmax()


profiles  = pd.concat(profile_list, axis = 1)
profiles = profiles.fillna(0).astype(int)


fw = open("consensus_output.txt", "w")
fw.write(consensus)
fw.write("\n")
fw.close()

with open("consensus_output.txt", 'a') as fa:
    profiles.to_csv(fa, mode = 'a' , sep = " ", header = False)
