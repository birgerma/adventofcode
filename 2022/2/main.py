# importing sys
import sys
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

if __name__=='__main__':
    print("Solve for problem 1 day 1")
    data = read_file('input.txt').split('\n')
