# Correct part1: 1635
# Correct part2: 58097428661390

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)
beams = '.'*len(data[0])
beams = list(beams)

# for line in data:
#     print(line)

init = data[0].index('S')

def part1():
    beams[init]='|'
    # print('beams:',beams)

    t = 1
    splits = set()
    while t<len(data):
        for i in range(len(beams)):
            if beams[i]=='|' and data[t][i]=='^':
                # print('Splitting the beam')
                splits.add((i,t))
                beams[i]='.'
                beams[i-1]='|'
                beams[i+1]='|'
                # print('New beams:', beams)
        t+=1

    # print(splits)
    print(len(splits))
    return len(splits)


from collections import defaultdict
def part2():
    # print('beams:',beams)
    beams = defaultdict(int)
    # beams = [init]
    beams[init] = 1
    t = 1
    while t<len(data):
        # next_beams = []
        keys = [k for k in beams.keys() if k>0]
        for i in keys:
            print('key:', i, 'val:', beams[i])
            if beams[i]==0:
                continue
            if data[t][i]=='^':
                print('Splitting the beam')
                # splits.add((i,t))
                n = beams[i]
                beams[i-1]+=n
                beams[i+1]+=n
                beams[i]-=n
                print(beams)
                # next_beams.append(i+1)
            # else:
            #     next_beams.append(i)
        t+=1
        # beams=next_beams

    # print(splits)
    # print(len(splits))
    # return len(splits)
    print(beams)
    print(len(beams))
    print(sum(beams.values()))
    return sum(beams.values())
    # return(len(beams))
# print('Solution part1:',part1())
print('Solution part2:',part2())
