
import sys

sys.path.append('../')

import utils.io_tools as io

data_file = './data1'

def solve1():
    entries = io.read_ints(data_file)
    
    count = 0

    for i in range(1, len(entries)):
        if(entries[i]>entries[i-1]):
            count+=1

    return count

def solve2():
    entries = io.read_ints(data_file)

    count = 0

    for i in range(1, len(entries)-2):
        j=i+1
        sum1 = sum(entries[i-1:i+2])
        sum2 = sum(entries[j-1:j+2])
        if(sum2>sum1):
            count+=1
    return count



sol1 = solve1()
assert sol1==1581
print("Solution 1:", sol1)

sol2 = solve2()
assert sol2==1618
print("Solution 2:", sol2)
