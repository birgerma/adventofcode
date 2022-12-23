# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def format_input(input):
    map = {}
    for y in range(len(input)):
        for x in range(len(input[y])):
            map[(x,y)]=input[y][x]
            #print(input[y][x], end='')
        #print()
    return map

from collections import defaultdict
def move_elfes(elf_map):
    print("=== Round","INIT",'===')
    draw_map(elf_map)
    n_it = 10
    order_index = 0
    #for it in range(n_it):
    it=1
    while it<=n_it:
        elfes= [coor for coor in elf_map if elf_map[coor]=='#']
        #count = defaultdict(lambda: 0)
        count = {}
        moves = []
        for x,y in elfes:
            #print("x,y", x,y)
            nw = (x-1, y-1)
            n= (x, y-1)
            ne = (x+1, y-1)
            s = (x, y+1)
            se = (x+1, y+1)
            sw = (x-1, y+1)
            w = (x-1, y)
            e = (x+1, y)
            
            checks = [
                [nw,n,ne],
                [s,se,sw],
                [w,nw,sw],
                [e,ne,se]
            ]
            next_dir = [n, s, w,e]
            if (not any([c in elfes for c in[nw, n, ne, s, se, sw, w, e]])):
                print(x,y,"No elfes near, wont move")
                continue

            new_coor = None
            for i in range(len(checks)):
                index = (i+order_index)%len(checks)
                check = checks[index]
                print("Check", index)
                if not any([c in elfes for c in check]):
                    print("PASS check", index, 'try move',x,y,'to', next_dir[index])
                    new_coor = next_dir[index]
                    break
            if new_coor is None:
                # Nowhere to move
                continue
            #if (not any([c in elfes for c in [n, nw, ne]])):
            #         new_coor = n
            #         print("Try move",x,y," NORTH to",new_coor)
            #elif (not any([c in elfes for c in [s, se, sw]])):
            #         new_coor = s
            #         print("Try move",x,y," SOUTH to",new_coor)
            #elif (not any([c in elfes for c in [w, nw, sw]])):
            #         new_coor = w
            #         print("Try move",x,y," WEST to",new_coor)
            #elif (not any([c in elfes for c in [e, ne, se]])):
            #         new_coor = e
            #         print("Try move",x,y," EAST to",new_coor)
            #else: # Do not suggest movement
            #    continue
            count[new_coor] = 2 if new_coor in count else 1
            moves.append((x,y,new_coor[0], new_coor[1]))
        for x,y,new_x, new_y in moves:
            print("Count:", new_x, new_y, count[(new_x, new_y)])
            if count[(new_x, new_y)]==1:
                print("Moving",x,y,"to", new_x, new_y)
                elf_map[(x,y)]='.'
                elf_map[(new_x, new_y)]='#'
                #print("Old coor:", elf_map[(x,y)])
                #print("New coor:", elf_map[(new_x, new_y)])
        print("=== Round",it,'===')
        draw_map(elf_map)
        order_index+=1
        it+=1
    return elf_map

def draw_map(elf_map):
    min_x = min([c[0] for c in elf_map])
    max_x = max([c[0] for c in elf_map])
    min_y = min([c[1] for c in elf_map])
    max_y = max([c[1] for c in elf_map])
    print("min x:", min_x, 'max_x:', max_x, 'min_y:',min_y, 'max_y:', max_y)
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) in elf_map:
                print(elf_map[(x,y)], end='')
            else:
                print('.', end='')
        print()

def count_score(elf_map):
    min_x = min([c[0] for c in elf_map if elf_map[c]=='#'])
    max_x = max([c[0] for c in elf_map if elf_map[c]=='#'])
    min_y = min([c[1] for c in elf_map if elf_map[c]=='#'])
    max_y = max([c[1] for c in elf_map if elf_map[c]=='#'])
    count = 0
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if (x,y) not in elf_map or elf_map[(x,y)]=='.':
            #if elf_map[(x,y)]=='.':
                count+=1
    return count


def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    elf_map = move_elfes(data)
    score = count_score(elf_map)
    print("Score:", score)
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
        partA(input, expected=4116)
    if case == 'b' or case == 'all':
        partB(input)


