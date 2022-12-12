# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

import igraph as graph

DAY = os.getcwd().split('/')[-1]

def get_height(char):
    if char=='S':
        return ord('a')
    elif char=='E':
        return ord('z')
    else:
        return ord(char)


def in_range(x,y, xmax, ymax):
    return x>=0 and y>=0 and x<xmax and y<ymax

def add_neighbours(x0,y0,vmap,grid,g):
    vid0 = vmap[(x0, y0)]
    neighbours = [(x0+1,y0), (x0-1,y0), (x0,y0+1), (x0,y0-1)]
    y_max = len(grid)
    x_max = len(grid[0])
    h0=get_height(grid[y0][x0])
    for n in neighbours:
        x=n[0]
        y=n[1]
        if (in_range(x,y,x_max, y_max)):
            h=get_height(grid[y][x])
            if (h0>=h-1):
                vid = vmap[(x,y)]
                g.add_edges([(vid0, vid)])
    return g

def format_input(input):
    y_max = len(input)
    x_max = len(input[0])
    n_vertices = y_max*x_max
    vmap = {}
    g = graph.Graph(directed=True)
    g.add_vertices(n_vertices)
    grid = []
    for row in input:
        grid.append(list(row))

    # Create map between coordinates and node id:s
    v_index=0
    S=None
    E=None
    for y in range(y_max):
        for x in range(x_max):
            v=grid[y][x]
            if v=='S':
                S=(x,y,v_index)
            if v=='E':
                E=(x,y,v_index)

            vmap[(x,y)]=v_index
            v_index+=1

    # Create edges
    for y in range(y_max):
        for x in range(x_max):
            v = grid[y][x]
            h=get_height(v)
            vid = vmap[(x,y)]
            g = add_neighbours(x,y,vmap,grid,g)


    return g, vmap, S, E

def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    g, vmap, S, E = format_input(input)
    path=g.get_shortest_paths(S[2],to=E[2],mode=graph.OUT,output='vpath')
    answear = len(path[0])-1
    
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
    print("Read raw:", raw)
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
    parser.add_argument('--raw', type=bool, nargs='?', default=False)
    args = parser.parse_args()
    print("Args:", args)
    input = get_input_data(args.filename, args.raw)
    case = args.case.lower()
    if case == 'a' or case == 'all':
        partA(input, expected=380)
    if case == 'b' or case == 'all':
        partB(input)


