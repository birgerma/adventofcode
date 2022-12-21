# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

values = {}
original_values = {}
def format_input(input):
    global values, original_values
    data = {}
    for line in input:
        line=line.split(": ")
        name = line[0]
        d = line[1]
        value = int(d) if d.isnumeric() else None
        d = d.split(" ")
        if value:
            values[name]=value
        data[name]=d
    original_values = values

    return data,values

def get_value(name, data):
    global values
    if name in values:
        return values[name]

    n1, op, n2 = data[name]
    v1 = get_value(n1, data)
    v2 = get_value(n2, data)

    if op=='+':
        values[name] = v1+v2
    elif op=='-':
        values[name]=v1-v2
    elif op=='*':
        values[name]=v1*v2
    elif op=='/':
        values[name]=v1/v2
    elif op=='==':
        print("Compare values", v1, 'and', v2,'. Is equal:', v1==v2)
        values[name] = [(v1==v2), v1, v2]

    return values[name]
# 3848301405791 too high
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data, values = format_input(input)
    root_val = get_value('root', data)
    answear = int(root_val)
    
    if answear:
        print("Solution for day {:} part A:".format(DAY),answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    global values
    data,_ = format_input(input)
    data['root'][1]='=='
    #print(data['root'])
    print("Start val:", values['humn'])
    start = 0 
    stop = 1000
    #for i in range(start, stop+1):
    i=3848301405791
    i = values['humn']
    inc = 1000000000
    while True:
        values = original_values.copy()
        print("Shouting", i)
        values['humn']=i
        check, v1, v2 = get_value('root', data)
        print("v1=", v1, 'v2=',v2, v1<v2, v1==v2)
        print()
        if check:
            print("Should shout:", i)
            break
        if v1<v2:
            print("too far, break")
            i=i-inc
            inc=int(inc/2)
            inc=1 if inc<1 else inc
            print("Uppdate inc:",inc)
        else:
            i+=inc
    if check:
        print("Found answear")
    else: 
        print("Try again")

    answear = None
    if answear:
        print("Solution for day {:} part B:".format(DAY),answear)
    if expected:
        assert answear==expected

def get_input_data(fname, raw):
    try:
        if raw:
            return read_file(fname)
        return read_list_data(fname)
    except FileNotFoundError as e:
        print("Exception:", e)
        return "" if raw else []

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Advent of code day {:}'.format(DAY))
    parser.add_argument('case', type=str, nargs='?', default='all', 
                        choices=['all', 'a', 'A', 'b', 'B'],
                        help='Solution for Advend of Code day')

    parser.add_argument('--filename', '-f', type=str, nargs='?', default='input.txt')
    parser.add_argument('--raw', type=bool, nargs=1, default=False)
    args = parser.parse_args()
    input = get_input_data(args.filename, args.raw)
    case = args.case.lower()
    if case == 'a' or case == 'all':
        partA(input, expected=38731621732448)
    if case == 'b' or case == 'all':
        partB(input, expected=3848301405790)


