# Correct part1: 694
# Correct day2: 

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname, remove_empty_lines=False)
split_index = data.index('')
print(split_index)

print(data)
ranges = data[:split_index]
articles = [int(a) for a in data[split_index+1:]]

from operator import itemgetter
def format_ranges(ranges):
    new_ranges = []
    for r in ranges:
        r = [int(x) for x in r.split('-')]
        new_ranges.append(r)

    return sorted(new_ranges, key=itemgetter(0))

ranges = format_ranges(ranges)
print(ranges)
print(articles)

def is_fresh(article, ranges):
    for r in ranges:
        if a<r[0]:
            continue
        if a<=r[1]:
            return True
    return False

fresh = []
for a in articles:
    if is_fresh(a, ranges):
        print(a,'is fresh')
        fresh.append(a)
print(fresh)
print(len(fresh))
