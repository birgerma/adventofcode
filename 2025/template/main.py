# Correct part1:
# Correct part2: 

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
# fname = 'data'
data = read_file(fname)

print(data)
