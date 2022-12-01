
import sys

sys.path.append('../')

import utils.io_tools as io

data_file = './data'

aim = 0
depth = 0
horizontal = 0

def parse_directions(data):
    directions = []
    for d in data:
        v = d.split(' ')
        dir = v[0]
        x = int(v[1])
        directions.append([dir, x])
    return directions

def update_pos(dir):
    global depth, aim, horizontal
    # print(dir[0], dir[1])
    print(aim, horizontal, depth)
    if (dir[0]=='forward'):
        horizontal+=dir[1]
        depth = depth + (aim*dir[1])
        # pos[0] = pos[0]+dir[1]
        # pos[2] = pos[2] + pos[1]*dir[1]
    elif (dir[0]=='up'):
        aim-=dir[1]
        print('aim:', aim)
        # pos[1] = pos[1]-dir[1]
    elif (dir[0]=='down'):
        aim+=dir[1]
        print('aim:', aim)
        # pos[1] = pos[1]+dir[1]

def solve2():
    data = io.read_file_lines(data_file)
    directions = parse_directions(data)
    for dir in directions:
        update_pos(dir)
        # print(dir, pos)
        # break
    return horizontal*depth
    # return pos[1]*pos[2]

sol2 = solve2()
# assert sol2==1618
print("Solution 2:", sol2)
