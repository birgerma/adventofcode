# importing sys
import sys
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, '../')
 
from common.io import *

if __name__=='__main__':
    print("Solve for problem 1 day 1")
    data = read_file('input.txt').split('\n')
    cal_sum = 0
    summation = []
    for d in data:
        if d=='':
            summation.append(cal_sum)
            cal_sum=0
        else:
            cal_sum+=int(d)
    maxSum = max(summation)
    assert maxSum==68775
    print("Answear to 1a:")
    print("Elf carrying most carries:", maxSum)

    summation = sorted(summation,reverse=True)
    print("Answear to 1b:")
    top3=summation[:3]
    print("Top 3 elves carrying a total of:", top3)
    assert top3==202585
