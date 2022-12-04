# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def partA(input):
    print("Solve for day {:d} part A".format(DAY))

def partB(item_list):
    print("Solve for day {:d} part B".format(DAY))

if __name__=='__main__':
    data_file = 'input.txt'
    item_list = read_list_data(data_file)
    partA(item_list)
    partB(item_list)

