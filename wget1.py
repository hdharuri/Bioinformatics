import wget
import collections

url = 'https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa'
wget.download(url,'lambda_virus.fa')

sequence = ''
with open('lambda_virus.fa', 'r') as f:
    for line in f:
        if not line[0] == '>':
            sequence += line.rstrip()

print('\n')
print(len(sequence))
