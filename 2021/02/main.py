
import sys

sys.path.append('../')

import utils.io_tools as io

data_file = './data'

def parse_directions(data):
    directions = []
    for d in data:
        v = d.split(' ')
        dir = v[0]
        x = int(v[1])
        directions.append([dir, x])
    return directions

def update_pos(pos, dir):
    # print(dir[0], dir[1])
    if (dir[0]=='forward'):
        pos[0] = pos[0]+dir[1]
    elif (dir[0]=='up'):
        pos[1] = pos[1]-dir[1]
    elif (dir[0]=='down'):
        pos[1] = pos[1]+dir[1]

    return pos

def solve1():
    pos = [0,0]
    data = io.read_file_lines(data_file)
    directions = parse_directions(data)
    for dir in directions:
        pos = update_pos(pos, dir)
        print(dir, pos)
        # break
    return pos[0]*pos[1]

def solve2():
    pass


sol1 = solve1()
# assert sol1==1581
print("Solution 1:", sol1)

sol2 = solve2()
# assert sol2==1618
print("Solution 2:", sol2)
