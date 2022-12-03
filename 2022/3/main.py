# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def find_common(lst1, lst2):
    set_items = set(lst1)
    for i in lst2:
        if i in set_items:
            return i
    

def compute_score(item):
    print(item, ord(item))
    if ord(item)>96:
        return ord(item)-96
    return ord(item)-38
    #print('a', ord('a')-96)
    #print('A', ord('A')-38)
    #return 0
def partA(item_list):
    print("Solve for day {:d} part A".format(DAY))
    common_items = []
    for entry in item_list:
        entry = list(entry)
        n=len(entry)
        first = entry[:n//2]
        second = entry[n//2:]
        common = find_common(first, second)
        common_items.append(common)

    score = 0
    for common in common_items:
        score+=compute_score(common)
    assert score==8085
    print("Score:", score)
   # print(item_list)

def partB(move_list):
    print("Solve for day {:d} part B".format(DAY))

if __name__=='__main__':
    data_file = 'input.txt'
    #data = read_file('test.txt')
    item_list = read_list_data(data_file)
    partA(item_list)
    #partB(item_list)

