# Correct day1: 44854383294
# Correct day2: 55647141923

import os, sys
sys.path.append('..')

from lib.io import read_file

# fname = 'test'
fname = 'data'
data = read_file(fname)[0].split(',')

def split_in_pieces(string, n_pieces):
    lst = []
    l=len(string)//n_pieces
    for i in range(0, len(string), l):
        lst.append(string[i:i+l])
    return lst

def is_valid_id_v2(id:int):
    id=str(id)
    N=len(id)
    # print('id:', id)
    # print('len=',N)
    for n in range(2,N+1):
        if N%n==0:
            # print('n=',n)
            pieces = split_in_pieces(id, n)
            is_valid=False
            for i in range(len(pieces)-1):
                # print(pieces[i], pieces[i+1])
                if pieces[i]!=pieces[i+1]:
                    is_valid=True
                    break
                # print('----')
            if not is_valid:
                return False
    return True
            # print(pieces)
    # print('Max n:', len(id)/2)
    # while n<=len(id)/2:
    #     i0=0
    #     while i0<len(id)/2:
    #         # print('i0:',i0)
    #         print('indexes 1:', i0, i0+n)
    #         print('indexes 2:', i0+n, i0+2*n)
    #         num1 = id[i0:i0+n]
    #         num2 = id[i0+n:i0+2*n]
    #         print('num1:',num1, 'num2:',num2)
    #         if len(num1)!=len(num2):
    #             exit(0)
    #         if num1[0]=='0' or num2[0]=='0':
    #             # print('Skipping')
    #             pass
    #         elif num1==num2:
    #             print('Is invalid')
    #             return False
    #         i0+=1
    #     n+=1
    # return True

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

def find_invalid_ids_v2(ids:list):
    invalid=[]
    for id in ids:
        valid = is_valid_id_v2(id)
        if not valid:
            invalid.append(id)
        # print('----')
    return invalid

invalid_ids = []
invalid_ids_v2 = []
# d = data[7]
# d=d.split('-')
# ids = list(range(int(d[0]),int(d[1])+1))
# invalid=find_invalid_ids(ids)
# print('Invalid ids:', invalid)
#     invalid=find_invalid_ids(ids)

# data = data[7:]
for d in data:
    d=d.split('-')
    # print(d)
    ids = list(range(int(d[0]),int(d[1])+1))
    invalid=find_invalid_ids(ids)
    # print('Invalid ids:', invalid)
    invalid_ids.append(invalid)


    invalid=find_invalid_ids_v2(ids)
    invalid_ids_v2.append(invalid)
    # break

# for i in invalid_ids_v2:
#     print(i)

import itertools
invalid_ids = list(itertools.chain.from_iterable(invalid_ids))
invalid_ids_v2 = list(itertools.chain.from_iterable(invalid_ids_v2))
# print(invalid_ids)
print(sum(invalid_ids))
print(sum(invalid_ids_v2))

