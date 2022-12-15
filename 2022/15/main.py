import json
import time
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

def get_max_r(data):
    r=float('-inf')
    for d in data:
        if d[4]>r:
            r=d[4]
    return r
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
    #draw_map(sensor_reach)
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
    y = 2000000
    intervals = []
    for sensor in data:
        r = sensor[4]
        dx = r-abs(y-sensor[1])

        if dx<0:
            continue
        x_start=sensor[0]-dx
        x_end = sensor[0]+dx
        intervals.append([x_start, x_end])
    merged = merge_intervals(intervals)

    count = 0
    for i in merged:
        dx = i[1]-i[0]
        count+=dx

    answear = count
    if answear:
        print("Solution for day {:} part A:".format(DAY),answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    data = format_input(input)

    min_x = 0
    min_y = 0
    max_x = 4000000
    max_y = 4000000

    for d in data:
        y_start = d[1]-d[4]
        y_end = d[1]+d[4]
        d.append(y_start)
        d.append(y_end)

    start_time = time.time()
    for y in range(min_y, max_y+1):
        intervals = []
        for sensor in data:
            if y<sensor[5] or y>sensor[6]:
                continue

            dx = sensor[4]-abs(y-sensor[1])
            intervals.append([sensor[0]-dx, sensor[0]+dx])
        if len(intervals)>1:
            i = merge_intervals(intervals)
            if len(i)>1:
                y_ans = y
                x_ans = i[0][1]+1

    print("--- %s seconds ---" % (time.time() - start_time))
    answear=x_ans*4000000+y_ans
    print("Answear:", answear)
    assert answear == expected

def merge_intervals(intervals):
    intervals=sorted(intervals)
    index=0
    while index<len(intervals)-1:
        i1 = intervals[index]
        i2 = intervals[index+1]
        if i1[1]<i2[0]:# Found non reached x
            index+=1
        elif i1[1]>=i2[1]: # i1 includes i2, remove i2
            del intervals[index+1]
        elif i1[1]>=i2[0]: # Overlapping, merge
            i1[1]=i2[1]
            intervals[index]=i1
            del intervals[index+1]
        else:
            print("Error")
            quit()
        if len(intervals)==1:
            break
    return intervals

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
    if case == 'test-a':
        testPartA(input)
    if case == 'test-b':
        testPartB(input)
    if case == 'a' or case == 'all':
        partA(input, expected=5335787)
    if case == 'b' or case == 'all':
        partB(input, expected=13673971349056)


