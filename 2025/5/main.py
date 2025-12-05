# Correct part1: 694
# Correct day2: 352716206375547

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

print(ranges)
def merge_ranges(ranges):
    i = 0
    while i<len(ranges)-1:
        r1 = ranges[i]
        r2 = ranges[i+1]
        print(r1,r2)
        if r1[1]>r2[0] or r1[1]==r2[0] or r1[1]+1==r2[0]:
            big = max(r1[1], r2[1])
            # print('r1',r1)
            # print('r2',r2)
            r_new = [r1[0], big]
            # print('New range:', r_new)
            # print("Old range list:", ranges)
            ranges[i+1]=r_new
            del ranges[i]
            # print('New range list:', ranges)
            # exit(0)
        else:
            i+=1
            # print('Increase i to',i)
            # print('len ranges:', len(ranges))
    return ranges

print(ranges)
min_a = ranges[0][0]
print(min_a)
for r in ranges:
    r[0]=r[0]-min_a
    r[1]=r[1]-min_a

print('------')
print(ranges)
# exit(0)
# debug = list()
# for i in ranges:
#     # print('r=', i)
#     # articles = list(range(i[0], i[1]+1))
#     a = i[0]
#     while a<=i[1]:
#         if not a in debug:
#             debug.append(a)
#         a+=1
#
# # print(debug)
# print(len(debug))
# exit(0)

print('Init ranges:', ranges)
ranges = merge_ranges(ranges)
print('Merged ranges:', ranges)
n_fresh = 0
for r in ranges:
    c = r[1]-r[0]+1
    n_fresh+=c



print(n_fresh)

