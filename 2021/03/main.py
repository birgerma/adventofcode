
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



test_data = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
def test():
    gamma, epsilon, power = get_diagnostics(test_data)
    assert power==198
    return int(power)

def get_most_common(data,pos, equal='1'):
    count=0
    for d in data:
        if(d[pos]=='1'):
            count+=1
    if (count==len(data)/2):
        return equal
    elif (count>len(data)/2):
        return '1'
    else:
        return '0'

def filter_bin(data, pos, keep):
    new = []
    for d in data:
        if d[pos]==keep:
            new.append(d)
    return new

def get_oxygen(data):
    for pos in range(len(data[0])):
        c = get_most_common(data,pos, equal='1')
        data = filter_bin(data,pos,c)
        if len(data)==1:
            break
    return data

def get_co2(data):
    for pos in range(len(data[0])):
        c = get_most_common(data,pos, equal='1')
        c = '1' if c=='0' else '0'
        data = filter_bin(data,pos,c)
        if len(data)==1:
            break
    return data


def test2():
    oxygen = int(get_oxygen(test_data)[0],2)
    co2 = int(get_co2(test_data)[0],2)
    return oxygen*co2


def solve1():
    data = io.read_file_lines(data_file)
    gamma, epsilon, power = get_diagnostics(data)
    return int(power)


def solve2():
    data = io.read_file_lines(data_file)
    oxygen = int(get_oxygen(data)[0],2)
    co2 = int(get_co2(data)[0],2)
    return oxygen*co2


assert test()==198
assert test2()==230
# print("Test solution:",test())
# print("Test2 solution:",test2())


sol1 = solve1()
assert sol1==4147524
print("Solution 1:", sol1)

sol2 = solve2()
assert sol2==3570354
print("Solution 2:", sol2)
