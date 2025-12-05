# Correct part1: 1428
# Correct day2: 

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)
for y in range(len(data)):
    data[y] = list(data[y])
#     print(data[y])
# exit(0)
import copy
move_map = copy.deepcopy(data)
W=len(data[0])
H=len(data)
print("Width:", W, 'Height:',H)
def get_neigbour_coor(x,y):
    delta = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
    neighbours = []
    for d in delta:
        x1 = x+d[0]
        y1 = y+d[1]
        # x1 = x+d[0]%W
        # y1 = y+d[1]%H
        # print(x1,y1)
        if 0<=x1<W and 0<=y1<H:
            neighbours.append((x1,y1))
    return neighbours


can_move = []
for y in range(H):
    for x in range(W):
        sym = data[y][x]
        print('x:',x,'y:',y,sym)
        if sym=='@':
            print('Found roll')
            neighbours = get_neigbour_coor(x,y)
            count=0
            if x==7 and y==0:
                print(neighbours)
            for (x1,y1) in neighbours:
                if x==7 and y==0:
                    print(x1,y1,data[y1][x1])
                if data[y1][x1]=='@':
                    count+=1
            print('Count:', count)
            if count<4:
                can_move.append((x,y))
                move_map[y][x]=str(count)
            # if x==7 and y==0:
            #     exit(0)

        print('----')

print(can_move)
print(len(can_move))


# for line in move_map:
#     print(line)
