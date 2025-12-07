# Correct part1: 4364617236318
# Correct part2: 9077004354241

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
# data = read_file(fname)
def format_part2(data):
    operators = data[-1]
    print(operators)

def do_op(op, nums):
    print('Do operation:')
    print(op,nums)
    print('-----')
    if op=='+':
        return sum(nums)
    else:
        print('Operator:', op)
        if op!='*':
            exit(0)
        s = 1
        for n in nums:
            s*=n
        return s
            

def part2():
    solutions = []
    with open(fname,'r') as f:
        data = f.readlines()
    for l in range(len(data)):
        print(list(data[l])[:-1])
        data[l] = list(data[l])[:-1]

    for line in data:
        print('>',line)
    # print(len(data))
    i = len(data[0])-1

    nums = []
    while i>=0:
        # print('>',data[0][i])
        num = ''
        print(len(data))
        for j in range(len(data)-1):
            # print(i,j)
            # print('num:',data[j][i])
            num += data[j][i]
        print("Final num:", num)
        # print(num.strip())
        if num.strip()=='':
            # print('Done, do operation')
            # print('Numbers:', nums)
            op = data[-1][i+1]
            # print('Operation:', op)
            s = do_op(op, nums)
            print('Solution:', s)
            solutions.append(s)
            nums = []
            # exit(0)
        elif i==0:
            print('Number to append:', num)
            nums.append(int(num))
            op = data[-1][i]
            # print('Operation:', op)
            s = do_op(op, nums)
            print('Solution:', s)
            solutions.append(s)
            nums = []
        else:
            print('Number to append:', num)
            nums.append(int(num))
        i-=1
    # format_part2(data)

    # print(solutions)
    print(sum(solutions))
    exit(0)

def part1():
    data = read_file(fname)
    problems = []
    for line in data:
        line = [l for l in line.split(' ') if l!='']
        problems.append(line)

    # print(problems)

    n = len(problems[0])
    m = len(problems)

    psum=0

    for x in range(n):
        op = problems[-1][x]
        v = 0 if op=='+' else 1
        # print('Operator:',op)
        for y in range(m-1):
            # print('problem:', x)
            # print(problems[y][x])
            if op == '+':
                v+=int(problems[y][x])
            else:
                v*=int(problems[y][x])

        # print(v)
        psum+=v
        # print('----')
    return psum

print('Solution part1:', part1())
print('Solution part2:', part2())



