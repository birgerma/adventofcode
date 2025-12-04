# Correct day1: 44854383294

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)[0].split(',')

# def is_valid_id(id:int):
#     id=str(id)
#     n=1
#     print('id:', id)
#     # print('n:',n)
#     # print('Max n:', len(id)/2)
#     while n<=len(id)/2:
#         i0=0
#         while i0<len(id)/2:
#             # print('i0:',i0)
#             num1 = id[i0:i0+n]
#             num2 = id[i0+n: i0+2+n]
#             print('num1:',num1, 'num2:',num2)
#             if num1[0]=='0' or num2[0]=='0':
#                 # print('Skipping')
#                 pass
#             elif num1==num2:
#                 print('Is invalid')
#                 return False
#             i0+=1
#         n+=1
#     return True
def is_valid_id(id:int):
    id=str(id)
    n=len(id)
    if n%2!=0:
        return True
    num1 = id[:n//2]
    num2 = id[n//2:]
    if num1[0]=='0':
        return True
    # print('id:',id, 'n1:', num1, 'n2:',num2)
    return num1!=num2


def find_invalid_ids(ids:list):
    invalid=[]
    for id in ids:
        valid = is_valid_id(id)
        if not valid:
            invalid.append(id)
        # print('----')
    return invalid


invalid_ids = []
# d = data[7]
# d=d.split('-')
# ids = list(range(int(d[0]),int(d[1])+1))
# invalid=find_invalid_ids(ids)
# print('Invalid ids:', invalid)
#     invalid=find_invalid_ids(ids)
for d in data:
    d=d.split('-')
    # print(d)
    ids = list(range(int(d[0]),int(d[1])+1))
    invalid=find_invalid_ids(ids)
    # print('Invalid ids:', invalid)
    invalid_ids.append(invalid)

# for i in invalid_ids:
#     print(i)

import itertools
invalid_ids = list(itertools.chain.from_iterable(invalid_ids))
# print(invalid_ids)
print(sum(invalid_ids))

