# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
from collections import defaultdict 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def as_int(char):
    num_chars = set(list("-+0123456789"))
    num = ""
    for i in range(len(char)):
        if char[i] in num_chars:
            num+=char[i]
    return int(num)

def parse_line(line):
    line = line.split(" ")
    line = [line[2], line[3], line[8], line[9]]
    line = [as_int(c.split("=")[1]) for c in line]
    return line

def format_input(input):
    coors = []
    for line in input:
        coor = parse_line(line)
        r = manhattan(coor[0], coor[1], coor[2], coor[3])
        coor.append(r)
        coors.append(coor)
    return coors


def manhattan(x1,y1, x2, y2):
    dx = abs(x1-x2)
    dy = abs(y1-y2)
    return dx+dy

def compute_sensor_reach(sensors, sensor_reach, line=0):
    print("Checking on line:", line)
    for sensor in sensors:
        sensor_x = sensor[0]
        sensor_y = sensor[1]
        beacon_x = sensor[2]
        beacon_y = sensor[3]
        #sensor_reach[(beacon_x, beacon_y)]=-1
        #sensor_reach[(sensor_x, sensor_y)]=-2
        #if sensor_x!=8 and sensor_y!=7: continue
        #r = manhattan(sensor_x, sensor_y, beacon_x, beacon_y)
        r = sensor[4]
        #print(sensor, r)
        dy = abs(sensor_y-line)
        x1 = sensor_x-r+dy
        x2 = sensor_x+r-dy
        #print(x1,x2)
        #max_x = max(x1,x2)
        #min_x = min(x1,x2)
        min_x = sensor_x-r
        max_x = sensor_x+r
        #print(min_x, max_x)
        for x in range(min_x, max_x+1):
            if manhattan(sensor_x,sensor_y,x,line)>r:
                continue
            if ((x,line) not in sensor_reach.keys()):
                #print("Mark", x, "as free")
                sensor_reach[(x,line)]=1
    return sensor_reach

def get_min_max(map):
    x_max=float('-inf')
    y_max=float('-inf')
    x_min=float('inf')
    y_min=float('inf')
    for (x,y) in map.keys():
        if x>x_max:
            x_max = x
        if x<x_min:
            x_min=x
        if y>y_max:
            y_max=y
        if y<y_min:
            y_min=y
    return x_min, x_max, y_min, y_max
def draw_map(sensor_map):
    cmap = {0:'.', 1:'#', -1:'B', -2:'S'}
    x_min, x_max, y_min, y_max = get_min_max(sensor_map)
    print(x_min, x_max, y_min,y_max)
    # Draw header:
    print("Header:")
    print("   ", end='')
    for x in range(x_min, x_max+1):
        if x>10:
            c = x//10
            print(c, end='')
        else:
            print(" ", end='')
    print()
    print("   ", end='')
    for x in range(x_min, x_max+1):
        if x<0:
            c = " "
        elif x>10:
            c=x%10
        else:
            c=x
        print(c,end='')
    print()
    for y in range(y_min, y_max+1):
        # Draw row number:
        print(y," ", end="")
        for x in range(x_min, x_max+1):
            v = sensor_map[(x,y)]
            c = cmap[v]
            print(c, end='')
        print()

def add_sensors_beacons(data, sensor_map):
    for sensor in data:
        sensor_x = sensor[0]
        sensor_y = sensor[1]
        beacon_x = sensor[2]
        beacon_y = sensor[3]
        sensor_map[(beacon_x, beacon_y)]=-1
        sensor_map[(sensor_x, sensor_y)]=-2

    return sensor_map

def get_max_r(data):
    r=float('-inf')
    for d in data:
        if d[4]>r:
            r=d[4]
    return r
import time
# 6160793 too high
# 5995319 too high
# 5335788 too high
def testPartA(input, expected=None):
    print("Testing for day {:} part A".format(DAY))
    data = format_input(input)
    max_r = get_max_r(data)
    sensor_reach = defaultdict(lambda:0)
    sensor_reach = add_sensors_beacons(data, sensor_reach)
    x_min, x_max, y_min, y_max = get_min_max(sensor_reach)
    DEBUG=False
    if DEBUG:
            sensor = data[-1]
            print(sensor)
            r = sensor[-1]
            y_min = y_min-max_r
            y_max = y_max+max_r
            #y_min = sensor[1]-r
            #y_max = sensor[1]+r
            for line in range(y_min, y_max+1):
                    sensor_reach = compute_sensor_reach(data, sensor_reach, line=line)
                    draw_map(sensor_reach.copy())
                    time.sleep(1)
            draw_map(sensor_reach)
            quit()
    line = 10
    #sensor_reach = compute_sensor_reach(data, sensor_reach, line=line)
    sensor_reach = compute_sensor_reach(data, sensor_reach, line=line)
    #print(sensor_reach)
    draw_map(sensor_reach)
    count = 0
    for (x,y) in sensor_reach.keys():
        if y==line and sensor_reach[(x,y)]==1:
            count+=1

    answear = count
    print("Answear:", answear)
    assert answear==26
    answear = None

def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    sensor_reach = defaultdict(lambda:0)
    sensor_reach = add_sensors_beacons(data, sensor_reach)
    line = 2000000
    sensor_reach = compute_sensor_reach(data, sensor_reach, line=line)
    count = 0
    for (x,y) in sensor_reach.keys():
        if y==line and sensor_reach[(x,y)]==1:
            count+=1

    answear = count
    #print(sensor_reach)
    #answear = len([no_beacon for no_beacon in sensor_reach.values() if no_beacon==1])
    print("Done", answear)       
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
                        choices=['all', 'a', 'A', 'b', 'B', 'test-a'],
                        help='Solution for Advend of Code day')

    parser.add_argument('--filename', '-f', type=str, nargs='?', default='input.txt')
    parser.add_argument('--raw', type=bool, nargs=1, default=False)
    args = parser.parse_args()
    input = get_input_data(args.filename, args.raw)
    case = args.case.lower()
    if case == 'test-a' or case == 'all':
        testPartA(input)
    if case == 'a' or case == 'all':
        partA(input, expected=5335787)
    if case == 'b' or case == 'all':
        partB(input)


