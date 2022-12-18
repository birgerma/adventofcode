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

def count_free_sides(grid, air=None):
    for p in grid.keys():
        neighbours = get_neighbours(p)
        for n in neighbours:
            if n in grid:
                grid[p]=grid[p]-1
            elif air and n in air:
                grid[p]=grid[p]-1
    return grid

def get_max(grid):
    dim = 3
    max_values = [float('-inf')]*dim
    for p in grid:
        for i in range(dim):
            if max_values[i]<p[i]:
                max_values[i]=p[i]
    return max_values

def get_min(grid):
    dim = 3
    min_values = [float('inf')]*dim
    for p in grid:
        for i in range(dim):
            if min_values[i]>p[i]:
                min_values[i]=p[i]
    return min_values

def is_outside(p, min_v, max_v):
    for i in range(len(p)):
        if min_v[i]>p[i] or max_v[i]<p[i]:
            return True
    return False

def rec_find_air_pockets(p,grid, min_vals, max_vals, path):
    if p in grid: # Is lava
        return path
    elif is_outside(p, min_vals, max_vals):
        return None
    else:
        for n in get_neighbours(p):
            new_path = rec_find_air_pockets(n, grid, min_vals, max_vals, path)
            if new_path==None: # found path to outside, no air pocket
                return None
            else:
                path+=new_path
        path.append(p)
        return path


def find_air_pockets(grid):
    max_values = get_max(grid)
    min_values = get_min(grid)
    air = {}
    for p in grid:
        for n in get_neighbours(p):
            path = rec_find_air_pockets(n, grid, min_values, max_values, [])
            if path is not None:
                for p in path:
                    air[p]=1
    return air
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
    grid = {}
    for p in data:
        grid[p]=6
    
    air = find_air_pockets(grid)
    print(air)
    grid = count_free_sides(grid, air=air)

    count = sum(grid.values())
    print("Count:", count)
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


