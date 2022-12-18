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
                #print("Add position:", pos)
                positions[pos]='#'
    return positions

def is_crash(x,y,rock,positions):
    for dy in range(len(rock)):
        for dx in range(len(rock[dy])):
            if rock[dy][dx]=='#':
                pos = (x+dx, y+dy)
                if pos in positions and positions[pos]=='#':
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

    #positions = defaultdict(lambda:'.')
    positions = {}
    for coor in floor:
        positions[coor] = '#'

    top = 0
    mem = {}
    #for rock_num in range(1,max_it+1):
    added = 0
    rock_num=0
    while rock_num<max_it:
        if rock_num%max_it/1000==0:
            print("Rock number:", rock_num, round(100*rock_num/max_it),"%")

        #top_layer = [c[1] for c in floor]
        #top = max(top_layer)
        y = top+3
        x = 2
        #print("Init coor:", x,y)
        rock = rocks[rock_index]
        rock_index= (rock_index+1)%len(rocks)

        bottom_found=False
        while not bottom_found:
            if rock_num>len(rocks):
                if False and rock_index==wind_index:
                    print("rock_index:", rock_index, "wind_index:", wind_index)
                    print("Top:", top, "rock_num:", rock_num)
                if False and rock_index==wind_index:
                    print("N winds:", len(wind))
                    print("Rock num:", rock_num)
                    print("Rock index:", wind_index)
                    print("Wind index:", wind_index)
                    print("Top:", top)
                    print("Equal index!")
                    # Could have found period
                    top_diff = top
                    period = rock_num
                    print("Period:", period)
                    fac = max_it//period
                    print("Fack:", fac)
                    tmp_rock = 0
                    tmp_top=0
                    while tmp_rock<max_it-period:
                        tmp_rock+=period
                        tmp_top+=top_diff
                    print("Expected:", 3068)
                    print(tmp_top-3068)
                    print("Test rock num:", tmp_rock)
                    print("Test top:", tmp_top)
                    top = tmp_top
                    y=top+3
                    diff = max_it-tmp_rock
                    print("Diff:", diff)
                    print("mem:", mem.keys())
                    print("To add:", mem[diff])
                    print(mem)
                    print("Final result:", top+mem[diff])
                    quit()
            # Push rock
            dx=wind[wind_index]
            #if dx>0:
            #    print("Push right")
            #else:
            #    print("Push left")
            x+=dx
            max_x = len(floor)-len(rock[0])
            #print("Max x:", max_x, len(floor)-1, len(rock[0]))
            if x>=max_x:
                x=max_x
            elif x<0:
                x=0

            wind_index = (wind_index+1)%len(wind)
            
            #print("x=",x, "y=",y)
            if is_crash(x,y,rock,positions):
                #print("Crash when blowing")
                x = x-dx

            # Rock falls
            #print("Rock falls")
            y-=1
            #print("x=",x, "y=",y)
            if is_crash(x,y,rock,positions):
                #print("Crash when falling")
                y_fin = y+1
                x_fin = x
                top = max(top, y_fin+len(rock))
                #mem[rock_num]=top
                bottom_found=True
                positions = add_rock(positions, x_fin,y_fin,rock)
                #print("Final x=",x_fin, "Final y=",y_fin, "top:",top)
                if False and rock_num<20:
                    draw_map(positions)

                top_layer = get_top_layer(positions)
                key = (rock_index, wind_index, str(top_layer))
                #print(key)
                # 1 514 285 714 288
                # 3068
                #if rock_num>2022 and key in mem:
                if added==0 and key in mem:
                    print("Found cycle")
                    print(mem[key])
                    prev_top, prev_rock_num = mem[key]
                    print("Rock num:", rock_num)
                    print("Prev top:", prev_top, "current top:", top)
                    dy = top-prev_top
                    dt = rock_num-prev_rock_num
                    print("dt=", dt, 'dy=', dy)
                    new_t = rock_num
                    it = 0
                    #while new_t<max_it-dt:
                    #    it+=1
                        #print(added)
                    #    new_t+=dt
                    #    added+=dy
                    #print("Sim it:", it)
                    #print("Sim new t:", new_t)
                    #print("Sim added:", added)
                    #print("max it", max_it, "prev_rock_num:", prev_rock_num, "dt:",dt)
                    it = (max_it-1-prev_rock_num)//dt
                    #print("Computed it:", it)
                    new_added = it*dy-dy
                    print("Computed added:", new_added)
                    print("Computed new t:", rock_num+it*dt-dt)

                    rock_num = rock_num+it*dt-dt
                    added = new_added

                    #quit()
                    #eadded = it*dy
                    #new_t = it*dt+prev_rock_num
                    #print("Computed it:", it)
                    #print("Computed new t:", new_t)
                    #print("Computed added:", added)
                    #print("Prev top:", prev_top)
                    #print("dt:", dt)
                    #print("dy:", dy)
                    #print("New t:", new_t)
                    #print("Max it:", max_it)
                    #eeprint("Added:", added)
                    #print("Added+prev:", added+prev_top)
                    #erock_num = new_t
                    #quit()
                    #amt = (max_it-1-prev_rock_num)//dt
                    #print(amt*dy)
                    #print("check:", added == amt*dy)
                    #quit()
                    #t += amt*dt
                    #print("Added:", added)
                    #print("Amt:", amt)
                    #print("left:", (max_it-1-prev_rock_num)%dt)
                    #print("Result?=", added+prev_top)
                    #print("Diff:", diff)
                    #print("rock_num:", rock_num)
                    #print("prev rock num:", prev_rock_num)
                    #quit()
                else:
                    mem[key]=(top,rock_num)
                break
        rock_num+=1
    print("Top:",top)
    print("Top+added:", top+added)
    return top+added
    quit()
    return positions

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
    #max_y=0
    #for pos in positions:
    #    if positions[pos]=='#':
    #        if pos[1]>max_y:
    #            max_y=pos[1]
    #answear = max_y+1
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
    answear = drop_the_rocks(rocks, floor, data, 1000000000000)
    
    
    #max_y=0
    #for pos in positions:
    #    if positions[pos]=='#':
    #        if pos[1]>max_y:
    #            max_y=pos[1]
    #answear = max_y+1


    #answear = None
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
        partB(input,1536994219669)


