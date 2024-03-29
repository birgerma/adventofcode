import time
                
from collections import defaultdict

import sys
import math
sys.path.append('../')

import utils.io_tools as io

data_file = './data'

def create_map(raw_data):
    data = raw_data.split('\n')
    map = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[i])):
            d = int(data[i][j])
            row.append(d)
        map.append(row)
    return map

def is_vertical_low(map, x, y):
    if y==0:
        return map[y][x]<map[y+1][x]
    elif y==len(map)-1:
        return map[y][x]<map[y-1][x]
    else:
        return map[y][x]<map[y+1][x] and map[y][x]<map[y-1][x]

def is_horizontal_low(map, x, y):
    if x==0:
        return map[y][x]<map[y][x+1]
    elif x==len(map[y])-1:
        return map[y][x]<map[y][x-1]
    else:
        return map[y][x]<map[y][x+1] and map[y][x]<map[y][x-1]


def is_low(map, x, y):
    return is_vertical_low(map, x, y) and is_horizontal_low(map, x, y)
    
def find_low_points(map):
    lows = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (is_low(map, x, y)):
                lows.append((x,y))
    return lows

def compute_risk(map, lows):
    risk = 0
    for x,y in lows:
        risk += map[y][x]+1
    return risk

def execution_time(func):
    start = time.time()
    res = func()
    end = time.time()
    print("Execution time:",end - start)
    return res

def compute_basin_size(map, x0, y0, x1=None, y1=None, basin=None):
    if (basin==None):
        basin = defaultdict(lambda: 0)
        basin = compute_basin_size(map, x0, y0, x0+1, y0, basin)
        basin = compute_basin_size(map, x0, y0, x0-1, y0, basin)
        basin = compute_basin_size(map, x0, y0, x0, y0+1, basin)
        basin = compute_basin_size(map, x0, y0, x0, y0-1, basin)
    else:
        if x1<0 or y1<0:
            return basin
        elif y1>len(map) or x1>len(map[y1]):
            return basin
        else:
            if map[y1][x1]==map[y0][x0]+1:
                basin[(x1,y1)]=1
                basin = compute_basin_size(map, x1, y1, x1+1, y1, basin)
                basin = compute_basin_size(map, x1, y1, x1-1, y1, basin)
                basin = compute_basin_size(map, x1, y1, x1, y1+1, basin)
                basin = compute_basin_size(map, x1, y1, x1, y1-1, basin)
            else:
                return basin
    return basin
    
test_data = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"
def test1():
    map = create_map(test_data)
    lows = find_low_points(map)
    risk = compute_risk(map, lows)
    return risk

def test2():
    pass

def solve1():
    data = io.read_file(data_file)
    map = create_map(data)
    lows = find_low_points(map)
    low = lows[0]
    risk = compute_risk(map, lows)
    return risk

def solve2():
    # data = io.read_file(data_file)
    data = test_data
    map = create_map(data)
    lows = find_low_points(map)
    low = lows[0]
    basin = compute_basin_size(map, low[0], low[1])
    print("Low:", low[0], low[1])
    print(basin)
    # return risk



# assert test()==
# assert test2()==
print("Test solution:",execution_time(test1))
# print("Test2 solution:",test2())


sol1 = solve1()
assert sol1==575
print("Solution 1:", sol1)

sol2 = solve2()
# assert sol2==3570354
print("Solution 2:", sol2)
