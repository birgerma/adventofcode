# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def format_input(input):
    data = []
    for c in list(input[0]):
        if c=='<':
            data.append(-1)
        elif c=='>':
            data.append(1)
    return data

def get_rocks():
    fname = "rocks.txt"
    raw_rocks = read_file(fname).split('\n')

    rock = []
    rocks = []
    for line in raw_rocks:
        if line=='':
            rocks.append(rock)
            rock=[]
        else:
            rock.append(list(line))

    return rocks

def create_floor(width):
    y=-1
    floor = []
    for x in range(width):
        floor.append((x,y))
    return floor

def add_rock(positions, x,y,rock):
    for dy in range(len(rock)):
        for dx in range(len(rock[dy])):
            if rock[dy][dx]=='#':
                pos = (x+dx, y+dy)
                positions[pos]='#'
    return positions

def is_crash(x,y,rock,positions):
    for dy in range(len(rock)):
        for dx in range(len(rock[dy])):
            if rock[dy][dx]=='#':
                pos = (x+dx, y+dy)
                if pos in positions and positions[pos]=='#':
                    return True
    return False

def draw_map(positions):
    max_x=6
    x_range = range(-1, max_x+2)
    max_y = max([p[1] for p in positions.keys()])

    for y in range(max_y, -1, -1):
        for x in x_range:
            if x<0 or x>max_x:
                c='|'
            else:
                c = positions[(x,y)]
            print(c,  end='')
        print()

def get_top_layer(positions):
    max_x=7
    top_layer=[]
    for x in range(max_x):
        y_max = max([pos[1] for pos in positions if pos[0]==x])
        top_layer.append(y_max)
    min_y = min(top_layer)
    top_layer = [y-min_y for y in top_layer]
    return top_layer

from collections import defaultdict
def drop_the_rocks(rocks, floor, wind, max_it):
    it = 0
    rock_index = 0
    wind_index = 0

    # Reverse rocks for simplicity:
    reversed = []
    for rock in rocks:
        reversed.append(rock[::-1])
    rocks = reversed

    positions = {}
    for coor in floor:
        positions[coor] = '#'

    top = 0
    mem = {}
    added = 0
    rock_num=0
    while rock_num<max_it:
        y = top+3
        x = 2
        rock = rocks[rock_index]
        rock_index= (rock_index+1)%len(rocks)

        bottom_found=False
        while not bottom_found:
            # Push rock
            dx=wind[wind_index]
            x+=dx
            max_x = len(floor)-len(rock[0])
            if x>=max_x:
                x=max_x
            elif x<0:
                x=0

            wind_index = (wind_index+1)%len(wind)
            if is_crash(x,y,rock,positions):
                x = x-dx

            # Rock falls
            y-=1
            if is_crash(x,y,rock,positions):
                y_fin = y+1
                x_fin = x
                top = max(top, y_fin+len(rock))
                bottom_found=True
                positions = add_rock(positions, x_fin,y_fin,rock)

                top_layer = get_top_layer(positions)
                key = (rock_index, wind_index, str(top_layer))
                if added==0 and key in mem:
                    prev_top, prev_rock_num = mem[key]
                    dy = top-prev_top
                    dt = rock_num-prev_rock_num
                    it = (max_it-1-prev_rock_num)//dt
                    added = it*dy-dy

                    rock_num = rock_num+it*dt-dt
                else:
                    mem[key]=(top,rock_num)
                break
        rock_num+=1
    return top+added

import time
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    rocks = get_rocks()
    WIDTH = 7
    floor = create_floor(WIDTH)
    start_time = time.time()
    answear = drop_the_rocks(rocks, floor, data, 2022)
    
    print("Answear:", answear)
    print("Computation time:", time.time()-start_time)
    if answear:
        print("Solution for day {:} part A:".format(DAY),answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    data = format_input(input)
    rocks = get_rocks()
    WIDTH = 7
    floor = create_floor(WIDTH)
    start_time = time.time()
    answear = drop_the_rocks(rocks, floor, data, 1000000000000)
    print("Computation time:", time.time()-start_time)
    
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
        partA(input, expected=3119)
    if case == 'b' or case == 'all':
        partB(input,1536994219669)


