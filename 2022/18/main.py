# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def format_input(input):
    points = []
    for coor in input:
        coor = coor.split(',')
        coor = [int(c) for c in coor]
        coor = (coor[0], coor[1], coor[2])
        points.append(coor)
    return points

def get_neighbours(p):
    n = []
    for dp in [-1,1]:
        n.append((p[0]+dp, p[1], p[2]))
        n.append((p[0], p[1]+dp, p[2]))
        n.append((p[0], p[1], p[2]+dp))
    return n

def count_free_sides(grid):
    for p in grid.keys():
        neighbours = get_neighbours(p)
        for n in neighbours:
            if n in grid:
                grid[p]=grid[p]-1

    return grid
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    grid = {}
    for p in data:
        grid[p]=6
    
    grid = count_free_sides(grid)
    answear = sum(grid.values())
    
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
        partA(input, expected=3564)
    if case == 'b' or case == 'all':
        partB(input)


