# Correct day1: 17383
# Correct day2: 172601598658203

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)

def get_max_jolt(num_lst, n=2):
    value = ''
    print(num_lst)
    prev_pos=-1

    for i in range(n,0,-1):
        N = len(num_lst)
        print("Should choose",i,"numbers from", N) 
        choices = num_lst[0:N-(i-1)]
        print("Choices:", choices)
        choice = max(choices)
        value+=choice
        print('Choosing:', choice)
        pos = num_lst.index(choice)
        print('Pos:', pos)
        num_lst = num_lst[pos+1:]
        print('New list:', num_lst)
        print('------')
    return value



    # print(num_lst)
    # print(len(num_lst))
    # print('Compare:',num_lst[0]+l1,'and',l2, '=>', m)
    # print('List 2:', num_lst[1:], 'n=', n)
    return num_lst


# Works for n=1, not otherwise
# def get_max_jolt(num_lst, n=1):
#     print(num_lst)
#     value=''
#     pos=-1
#     N=len(num_lst)
#     for i in range(n,-1,-1):
#         # print(i)
#         v = max(num_lst[pos+1:N-i])
#         pos = num_lst.index(v)
#         # print('v=',v)
#         # print('pos:', pos)
#         # value.append(v)
#         # value+=v*10*(i+1)
#         value+=v
#     print('Found max:', value)
#     return int(value)
# print(data)
jolt = []
jolt_2 = []
# data = [data[1]]
for d in data:
    jolt.append(int(get_max_jolt(d)))
    jolt_2.append(int(get_max_jolt(d, n=12)))
    # exit(0)
# for d in data:
#     d = [int(x) for x in d]
#     n = len(d)
#     n1 = max(d[0:n-1])
#     pos = d.index(n1)
#     n2 = max(d[pos+1:])
#     num = n1*10 + n2
#     print('num:', num)
#     jolt.append(num)
#
print(jolt)
print(jolt_2)
print(sum(jolt))
print(sum(jolt_2))
