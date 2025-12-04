# Correct day1: 17383
# Correct day2: 

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)

# print(data)
jolt = []
d = data[0]
for d in data:
    d = [int(x) for x in d]
    n = len(d)
    n1 = max(d[0:n-1])
    pos = d.index(n1)
    n2 = max(d[pos+1:])
    num = n1*10 + n2
    print('num:', num)
    jolt.append(num)

print(sum(jolt))
