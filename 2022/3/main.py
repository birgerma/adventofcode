# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def partA(move_list):
    print("Solve for day {:d} part A".format(DAY))
  
def partB(move_list):
    print("Solve for day {:d} part B".format(DAY))

if __name__=='__main__':
    data = read_file('input.txt')
    move_list = read_list_data('input.txt')
    partA(move_list)
    partB(move_list)

