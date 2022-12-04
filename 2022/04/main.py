# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def as_ints(lst):
    ints = []
    for i in lst:
        ints.append(int(i))
    return ints

def format_input(input):
    formated = []
    for i in input:
        i = i.split(',')
        first = i[0].split('-')
        second = i[1].split('-')
        first = as_ints(first)
        second = as_ints(second)
        formated.append([first, second])
        #print(first, second)
    return formated

def is_in(p1, p2):
    return p1[0]<=p2[0] and p1[1]>=p2[1]

def is_contained(p1, p2):
    return is_in(p1,p2) or is_in(p2,p1)
        
def partA(input):
    print("Solve for day {:d} part A".format(DAY))
    pair_list = format_input(input)
    count = 0
    for pair in pair_list:
        if is_contained(pair[0], pair[1]):
            count+=1
    assert count==584
    print("Number of overlapping pairs:",count)

def partB(item_list):
    print("Solve for day {:d} part B".format(DAY))

# 508 too low
if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    partA(item_list)
    #partB(item_list)


