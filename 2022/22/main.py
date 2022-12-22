# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def format_directions(input):
    directions = []
    tmp = ''
    for d in input:
        if d in 'LRUD':
            directions.append(int(tmp))
            directions.append(d)
            tmp=''
        else:
            tmp+=d
    directions.append(int(tmp))
    return directions

def format_input(input):
    directions = input[-1]
    raw_map = input[:-1]
    map = {}
    for y in range(len(raw_map)):
        line = raw_map[y]
        for x in range(len(line)):
            c = line[x]
            if c==' ':
                pass
                #print('_', end='')
            elif c=='.':
                #print(c, end='')
                map[(x,y)]=0
            elif c=='#':
                #print(c, end='')
                map[(x,y)]=1
            else:
                print("Error")
                quit()
        #print()
    directions = format_directions(directions)
    return map, directions

def find_start(map):
    return min([coor for coor in map if coor[1]==0])

def get_next(x0,y0, dir, map):
    delta_map = {'L':(-1, 0), 'R':(1,0), 'U':(0,-1), 'D':(0,1)}
    delta = delta_map[dir]
    max_x = max([i[0] for i in map])
    max_y = max([i[1] for i in map])
    x = x0+delta[0]
    y = y0+delta[1]
    if (x,y) not in map:
        print("not in map")
        if x<x0:
            print("Wrap around x left to right")
            x = max([i[0] for i in map if i[1]==y])
        elif x>x0:
            print("Wrap around x")
            x=min([i[0] for i in map if i[1]==y])
        if y<y0:
            y = max([i[1] for i in map if i[0]==x])
        elif y>y0:
            print("Wrap around y")
            y=min([i[1] for i in map if i[0]==x])
    if map[(x,y)]==0:
        return x,y
    print("Is wall, return None")
    return None

def draw_map(map, path):
    x0,y0=0,0
    x_max = max([i[0] for i in map])
    y_max = max([i[1] for i in map])
    for p in path:
        if p[2]=='R':
            c = '>'
        elif p[2]=='D':
            c='v'
        elif p[2]=='U':
            c='^'
        elif p[2]=='L':
            c='<'
        map[(p[0],p[1])]=c
    for y in range(y0, y_max+1):
        for x in range(x0, x_max+1):
            if (x,y) in map:
                if map[(x,y)]==0:
                    print('.', end='')
                elif map[(x,y)]==1:
                    print('#', end='')
                else:
                    print(map[(x,y)], end='')
            else:
                print(" ", end='')
        print()
def move(x0, y0, directions, map):
    dir = 'R'
    turn_right = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
    turn_left = {'U':'L', 'L':'D', 'D':'R', 'R':'U'}
    path = [(x0, y0, dir)]
    x,y = x0,y0
    for d in directions:
        print("Movement:", d)
        if type(d) is int:
            print("Current:", x0, y0)
            print("Move", d, "steps")
            steps = d
            while steps>0:
                coor = get_next(x,y, dir, map)
                if coor is None:
                    print("Walked into wall, stop")
                    steps = 0
                    break
                x,y = coor
                steps-=1
                path.append((x,y,dir))
                print("Next:", x,y, "steps left:", steps)
        else:
            print("Turn to the", d)
            if d=='R':
                dir = turn_right[dir]
            else:
                dir = turn_left[dir]
            path.append((x,y,dir))
            print("New direction", dir)
    #draw_map(map, path)
    return path
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    map, directions = format_input(input)
    x0, y0 = find_start(map)
    path = move(x0, y0, directions, map)
    final = path[-1]
    print(final)
    x = final[0]+1
    y = final[1]+1
    dir = final[2]
    print("Final dir:", dir)
    dir_score = {'R':0, 'D':1, 'L':2, 'U':3}[dir]
    print("Dir score:", dir_score)
    score = y*1000 + x*4 + dir_score

    print(score)
    answear = None
    
    if answear:
        print("Solution for day {:} part A:".format(DAY),answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    data = format_input(input)

    answear = None
    if answear:
        print("Solution for day {:} part B:".format(DAY),answear)
    if expected:
        assert answear==expected

def get_input_data(fname, raw):
    try:
        if raw:
            return read_file(fname)
        return read_list_data(fname)
    except FileNotFoundError as e:
        print("Exception:", e)
        return "" if raw else []

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Advent of code day {:}'.format(DAY))
    parser.add_argument('case', type=str, nargs='?', default='all', 
                        choices=['all', 'a', 'A', 'b', 'B'],
                        help='Solution for Advend of Code day')

    parser.add_argument('--filename', '-f', type=str, nargs='?', default='input.txt')
    parser.add_argument('--raw', type=bool, nargs=1, default=False)
    args = parser.parse_args()
    input = get_input_data(args.filename, args.raw)
    case = args.case.lower()
    if case == 'a' or case == 'all':
        partA(input, expected)
    if case == 'b' or case == 'all':
        partB(input)


