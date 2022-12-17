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
        else:
            print("ERROR")
            quit()
    return data

def get_rocks():
    fname = "rocks.txt"
    raw_rocks = read_file(fname).split('\n')

    rock = []
    rocks = []
    for line in raw_rocks:
        if line=='':
            print("New rock")
            rocks.append(rock)
            rock=[]
        else:
            rock.append(list(line))
            print(line)

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
            #print(dy,dx,rock[dy][dx])
            if rock[dy][dx]=='#':
                pos = (x+dx, y+dy)
                print("Add position:", pos)
                positions[pos]='#'
    return positions

def is_crash(x,y,rock,positions):
    for dy in range(len(rock)):
        for dx in range(len(rock[dy])):
            if rock[dy][dx]=='#':
                pos = (x+dx, y+dy)
                if positions[pos]=='#':
                    #print("pos", pos, "is rock:", positions[pos])
                    #top = y+1+len(rock)
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

from collections import defaultdict
def drop_the_rocks(rocks, floor, wind, max_it):
    it = 0
    rock_index = 0
    wind_index = 0
    print(wind)

    # Reverse rocks for simplicity:
    reversed = []
    for rock in rocks:
        reversed.append(rock[::-1])
    rocks = reversed

    positions = defaultdict(lambda:'.')
    for coor in floor:
        positions[coor] = '#'

    top = 0
    for rock_num in range(1,2023):
        print("Rock number:", rock_num)
        #top_layer = [c[1] for c in floor]
        #top = max(top_layer)
        y = top+3
        x = 2
        print("Init coor:", x,y)
        rock = rocks[rock_index]
        rock_index= (rock_index+1)%len(rocks)

        bottom_found=False
        while not bottom_found:
            # Push rock
            dx=wind[wind_index]
            if dx>0:
                print("Push right")
            else:
                print("Push left")
            x+=dx
            max_x = len(floor)-len(rock[0])
            #print("Max x:", max_x, len(floor)-1, len(rock[0]))
            if x>=max_x:
                x=max_x
            elif x<0:
                x=0

            wind_index = (wind_index+1)%len(wind)
            
            print("x=",x, "y=",y)
            if is_crash(x,y,rock,positions):
                print("Crash when blowing")
                x = x-dx

            # Rock falls
            print("Rock falls")
            y-=1
            print("x=",x, "y=",y)
            if is_crash(x,y,rock,positions):
                print("Crash when falling")
                y_fin = y+1
                x_fin = x
                top = max(top, y_fin+len(rock))
                bottom_found=True
                positions = add_rock(positions, x_fin,y_fin,rock)
                print("Final x=",x_fin, "Final y=",y_fin, "top:",top)
                if rock_num<20:
                    draw_map(positions)
                break
    return positions

def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    rocks = get_rocks()
    WIDTH = 7
    floor = create_floor(WIDTH)
    positions = drop_the_rocks(rocks, floor, data, 2022)
    
    max_y=0
    for pos in positions:
        if positions[pos]=='#':
            if pos[1]>max_y:
                max_y=pos[1]
    answear = max_y+1
    #correct: 3119  
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
    print("Args:", args)
    input = get_input_data(args.filename, args.raw)
    print("input:", input)
    case = args.case.lower()
    if case == 'a' or case == 'all':
        partA(input, expected=3119)
    if case == 'b' or case == 'all':
        partB(input)


