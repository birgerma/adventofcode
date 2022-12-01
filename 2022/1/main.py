# importing sys
import sys
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '../')
 
from common.io import *

if __name__=='__main__':
    print("Solve for problem 1 day 1")
    data = read_file('input.txt').split('\n')
    sum = 0
    maxSum = 0
    for d in data:
        if d=='':
            print("New elf")
            if(sum>maxSum):
                maxSum = sum
            sum=0
        else:
            sum+=int(d)
    print(maxSum)
