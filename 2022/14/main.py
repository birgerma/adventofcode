# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from collections import defaultdict

from common.io import *

DAY = os.getcwd().split('/')[-1]

def format_nodes(str_nodes):
    formated = []
    for node in str_nodes:
        node = node.strip()
        coor = node.split(",")
        x = int(coor[0])
        y = int(coor[1])
        formated.append((x,y))
    return formated
def format_input(input):
    print_list(input)
    formated = []
    for row in input:
        raw_nodes = row.split("->")
        nodes = format_nodes(raw_nodes)
        formated.append(nodes)
    return formated

def abs(x):
    if x<0:
        return -x
    return x

def norm(x):
    if x>0:
        return 1
    elif x==0:
        return 0
    else:
        return -1

def get_points(p1, p2):
    x1=min(p1[0], p2[0])
    y1=min(p1[1], p2[1])
    x2=max(p1[0], p2[0]) 
    y2=max(p1[1], p2[1])
    dx = norm(x2-x1)
    dy = norm(y2-y1)
    print(dx,dy)
    print("p1:", x1,y1)
    print("p2:", x2,y2)
    x=x1
    y=y1
    print(x<=x2, y<=y2)
    points = []
    while (x<=x2 and y<=y2):
        points.append((x,y))
        print("Point:", x,y)
        x+=dx
        y+=dy
    return points

def add_rocks(points, cave_map):
    rock=1
    for point in points:
        cave_map[point]=rock
    return cave_map

def create_cave(rock_coor):
    cave_map = defaultdict(lambda:0)
    for row in rock_coor:
        print("Row:", row)
        for i in range(len(row)-1):
            print("Pair:", row[i], row[i+1])
            points = get_points(row[i], row[i+1])
            cave_map = add_rocks(points, cave_map)
    print(cave_map)
    return cave_map

def get_max_y(coor_map):
    coor = coor_map.keys()
    max_y=float('-inf')
    for c in coor:
        y=c[1]
        if y>max_y:
            max_y=y
    return max_y

def print_cave(cave_map, start):
    char_map = {0:".", 1:"#", 2:"o",3:"+"}
    cave_map[start]=3
    x_values = [coor[0] for coor in cave_map.keys()]
    y_values = [coor[1] for coor in cave_map.keys()]
    for y in range(min(y_values), max(y_values)+1):
        for x in range(min(x_values), max(x_values)+1):
            v = cave_map[(x,y)]
            c = char_map[v]
            print(c,end='')
        print()
def add_sand(start, cave_map):
    min_rock = get_max_y(cave_map)
    print("Min y:", min_rock)
    x=start[0]
    y=start[1]
    while y<min_rock:
        # check coordinates below:
        if cave_map[(x, y+1)]==0:
            # Ok do go down
            y=y+1
        elif cave_map[(x-1,y+1)]==0: # Check down to the left
            # Ok do go here
            x=x-1
            y=y+1
        elif cave_map[(x+1, y+1)]==0:
            x=x+1
            y=y+1
        else:
            # Found bottom, return
            break
    print("Final coordinates:", x,y)
    return (x,y)


import time
def pour_sand(start, cave_map):
    min_rock = get_max_y(cave_map)
    while True:
        coor = add_sand(start, cave_map)
        print(coor)
        if coor[1]>=min_rock or coor[1]<=start[1]:
            print("Sand not resting anymore")
            break
        cave_map[coor]=2
        #print_cave(cave_map, start)
        #time.sleep(2)
    return cave_map

def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    cave_map = create_cave(data)
    cave_map = pour_sand((500,0), cave_map)
    sand = [s for s in cave_map.values() if s==2]
    print("Sand:", len(sand))
    answear = len(sand)
    
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
        partA(input, expected=795)
    if case == 'b' or case == 'all':
        partB(input)


