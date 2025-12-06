# Correct part1: 4364617236318
# Correct part2: 

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)

problems = []
for line in data:
    line = [l for l in line.split(' ') if l!='']
    problems.append(line)

# print(problems)

n = len(problems[0])
m = len(problems)

psum=0

for x in range(n):
    op = problems[-1][x]
    v = 0 if op=='+' else 1
    # print('Operator:',op)
    for y in range(m-1):
        # print('problem:', x)
        # print(problems[y][x])
        if op == '+':
            v+=int(problems[y][x])
        else:
            v*=int(problems[y][x])

    # print(v)
    psum+=v
    # print('----')

print(psum)



