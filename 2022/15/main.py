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
def testPartB(input, expected=None):
    print("Testing for day {:} part A".format(DAY))
    data = format_input(input)
    min_x = 0
    min_y = 0
    max_x = 20
    max_y = 20

    sensor_reach = defaultdict(lambda:0)
    sensor_reach = add_sensors_beacons(data, sensor_reach)

    coor = None
    for sensor in data:
        print("Sensor:", sensor)
        r = sensor[4]
        x_start = max(min_x, sensor[0]-r)
        x_end = min(max_x, sensor[0]+r)
        y_start = max(min_y, sensor[1]-r)
        y_end = min(max_y, sensor[1]+r)
        print(x_start, x_end, y_start, y_end)
        for y in range(y_start, y_end+1):
            print("y=", y)
            dy = (abs(y-sensor[1]))
            dx = abs(abs(y-sensor[1])-r)
            print("Init:", x_start, x_end)
            x_start=max(min_x, sensor[0]-dx)
            x_end = min(max_x, sensor[0]+dx)
            print("Update:", x_start, x_end)
            print("dx:", dx, "dy:", dy,"r=",r)
            continue
            quit()
            for x in range(x_start, x_end+1):
                if (x,y) not in sensor_reach:
                    if manhattan(x,y,sensor[0], sensor[1])<=r:
                        sensor_reach[(x,y)]=1
        quit()
    for x in range(max_x+1):
        for y in range(max_y+1):
            if (x,y) not in sensor_reach:
                coor = (x,y)
    answear = coor[0]*4000000+coor[1]
    print("Test b:", answear)
    assert answear==56000011

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

import json
def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    data = format_input(input)

    min_x = 0
    min_y = 0
    max_x = 4000000
    max_y = 4000000

    sensor_reach = defaultdict(lambda:0)
    sensor_reach = add_sensors_beacons(data, sensor_reach)
    coor = None
    intervals = {}
    for sensor in data:
        print("Checking sensor:", sensor)
        r = sensor[4]
        y_start = max(min_y, sensor[1]-r)
        y_end = min(max_y, sensor[1]+r)

        for y in range(y_start, y_end+1):
            if not y in intervals:
                intervals[y]=[]
            dy = (abs(y-sensor[1]))
            dx = abs(abs(y-sensor[1])-r)

            x_start=max(min_x, sensor[0]-dx)
            x_end = min(max_x, sensor[0]+dx)
            intervals[y].append([x_start,x_end])

    for y in intervals.keys():
        i = merge_intervals(intervals[y])
        if len(i)>1:
            print(y, i)
            y_ans = y
            x_ans = i[0][1]+1
            print()
            break
    answear=x_ans*4000000+y
    print("Answear:", answear)
    assert answear == expected
    quit()

    print("All checked, find answear")
    y=3349056
    x=3418491+1
    answear = x*4000000+y
    # Serializing json
    json_object = json.dumps(intervals, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    quit()
    print("Number of rows:", len(intervals.keys()))
    for y in intervals.keys():
        print(y)
        print(intervals[y])
    quit()
    for x in range(max_x+1):
        for y in range(max_y+1):
            if (x,y) not in sensor_reach:
                coor = (x,y)
    answear = coor[0]*4000000+coor[1]
    if answear:
        print("Solution for day {:} part B:".format(DAY),answear)
    if expected:
        assert answear==expected

def merge_intervals(intervals):
    intervals=sorted(intervals)
    while True:
        i1 = intervals[0]
        i2 = intervals[1]
        if i1[1]<i2[0]:# Found non reached x
            #print("Done:", i1[1], i1[0])
            return [i1, i2]
        elif i1[1]>=i2[1]: # i1 includes i2, remove i2
            del intervals[1]
        elif i1[1]>=i2[0]: # Overlapping, merge
            i1[1]=i2[1]
            intervals[0]=i1
            del intervals[1]
        else:
            print("Error")
            quit()
        #print(i1, i2)
        if len(intervals)==1:
            break
    #print(intervals)
    return intervals

def b_from_file():
    y=3349056
    x=3418491+1
    print(x*4000000+y)
    quit()
    # Opening JSON file
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    intervals = json_object
    print("N keys:", len(intervals.keys()))

    for y in intervals.keys():
        #print(intervals[y])
        #print(y)
        i = merge_intervals(intervals[y])
        print(i)
        if len(i)>1:
            print(y, i)
            print()
            break
        
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
                        choices=['all', 'a', 'A', 'b', 'B', 'test-a', 'test-b'],
                        help='Solution for Advend of Code day')

    parser.add_argument('--filename', '-f', type=str, nargs='?', default='input.txt')
    parser.add_argument('--raw', type=bool, nargs=1, default=False)
    args = parser.parse_args()
    input = get_input_data(args.filename, args.raw)
    case = args.case.lower()
    if case == 'test-a' or case == 'all':
        testPartA(input)
    if case == 'test-b' or case == 'all':
        testPartB(input)
    if case == 'a' or case == 'all':
        partA(input, expected=5335787)
    if case == 'b' or case == 'all':
        #b_from_file()
        #quit()
        partB(input, expected=13673971349056)


