# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def find_start(stream, n=4):
    for i in range(0, len(stream)-4):
        s = set(stream[i:i+n])
        print(stream[i:i+n])
        print(s)
        print(len(s))
        if len(s)==n:
            return i+n

def partA(input, expected=None):
    print("Solve for day {:d} part A".format(DAY))
    start = find_start(input)
    if expected:
        assert start==expected
    print("Result:", start)

def partB(input, expected=None):
    print("Solve for day {:d} part B".format(DAY))
    start = find_start(input, n=14)
    if expected:
        assert start==expected
    print("Result:", start)
if __name__=='__main__':
    TEST=False
    if TEST:
        data = read_list_data('test.txt')
        PART='A'
        if PART=='A':
            expected = [7, 5, 6, 10, 11]
            for i in range(len(data)):
                partA(data[i], expected[i])
        elif PART=='B':
            expected = [19, 23, 23, 29, 29]
            for i in range(len(data)):
                partB(data[i], expected[i])
    else:
            data_file = 'input.txt'
            item_list = read_file(data_file)
            partA(item_list, 1647)
            partB(item_list, 2447)

