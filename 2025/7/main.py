# Correct part1: 1635
# Correct part2: 

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)
beams = '.'*len(data[0])
beams = list(beams)

for line in data:
    print(line)

init = data[0].index('S')
beams[init]='|'
print('beams:',beams)

t = 1
splits = set()
while t<len(data):
    for i in range(len(beams)):
        if beams[i]=='|' and data[t][i]=='^':
            print('Splitting the beam')
            splits.add((i,t))
            beams[i]='.'
            beams[i-1]='|'
            beams[i+1]='|'
            print('New beams:', beams)
    t+=1

print(splits)
print(len(splits))
