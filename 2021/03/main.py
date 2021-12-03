
import sys
import math
sys.path.append('../')

import utils.io_tools as io

data_file = './data'

def compute_most_common(data):
    count = [0]*len(data[0])
    for num in data:
        for i in range(len(num)):
            if num[i]=='1':
                count[i]+=1
    for j in range(len(count)):
        if (count[j]>len(data)/2):
            count[j]=1
        else:
            count[j]=0
    return count

def bin_invert(bin_lst):
    inverted = []
    for b in bin_lst:
        inverted.append(abs(b-1))
    return inverted

def bin_lst_to_dec(bin_lst):
    dec = 0
    e=len(bin_lst)-1
    for n in bin_lst:
        dec+=n*math.pow(2,e)
        e-=1
    return dec

def get_diagnostics(data):
    common = compute_most_common(data)
    uncommon = bin_invert(common)
    
    gamma = bin_lst_to_dec(common)
    epsilon = bin_lst_to_dec(uncommon)
    power = gamma*epsilon
    return gamma, epsilon, power


def solve1():
    data = io.read_file_lines(data_file)
    gamma, epsilon, power = get_diagnostics(data)
    return int(power)


def solve2():
    pass


def test():
    data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
    gamma, epsilon, power = get_diagnostics(data)
    assert power==198
    return int(power)

print("Test solution:",test())


sol1 = solve1()
# # assert sol1==1581
print("Solution 1:", sol1)

# sol2 = solve2()
# # assert sol2==1618
# print("Solution 2:", sol2)
