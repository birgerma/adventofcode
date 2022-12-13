# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def parse(string, start=1):
    lst = []
    str_num = ""
    i=start
    while i<len(string):
        c = string[i]
        i+=1
        if c==',':
            if str_num!="":
                lst.append(int(str_num))
            str_num=""
        elif c=='[':
            nested, new_i = parse(string, start=i)
            lst.append(nested)
            i=new_i
        elif c==']':
            if str_num!="":
                lst.append(int(str_num))
            break
        else:
            str_num+=c
    
    return lst, i

def format_input(input):
    raw_pairs = input.split('\n\n')
    pairs = []
    for raw_pair in raw_pairs:
        pairs.append(raw_pair.split('\n'))

    formated = []
    for i in range(len(pairs)):
        pair = pairs[i]
        left,_ = parse(pair[0])
        right,_ = parse(pair[1])
        formated.append((left,right))
    return formated

def check_order(pair,do_print=False, tab_level=''):
    left = pair[0]
    right = pair[1]
    if do_print:
        print(tab_level, "-Compare", left,"vs",right)
    for i in range(len(left)):
        if i<len(right):
            l = left[i]
            r = right[i]
            if do_print:
                print(tab_level, " -Compare",l,'vs', r)
                
            if type(l)!=type(r):
                #print("Different types, converting")
                l = [l] if isinstance(l,int) else l
                r = [r] if isinstance(r,int) else r

            if isinstance(l, int) and isinstance(r,int):
                if l<r:
                    if do_print:
                        print(tab_level, "  - Left side smaller, so inputs are in the right order")
                    return True
                elif l>r:
                    if do_print:
                        print(tab_level, "  - Right side is smaller, so inputs are not in the right order")
                    return False
                else:
                    pass
            elif isinstance(l, list) and isinstance(r,list):
                res = check_order((l,r),do_print, tab_level+'\t')
                if res==None:
                    continue
                return res
            else:
                print("Should not be here!")
                quit()

        else:
            if do_print:
                print(tab_level, "- Right side ran out of items, so inputs are not in the right order")
            return False

    if do_print:
        print(tab_level, " - Left side ran out of items, so inputs are in the right order")
    # Check if both lists are of equal length:
    if isinstance(left,list) and len(left)==len(right):
        return None
    return True
            
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    do_print=False
    answear = 0
    for i in range(len(data)):
        pair = data[i]
        if do_print:
            print("== Pair", i+1, "==")
        res = check_order(pair,do_print=do_print)
        if do_print:
            print("Is in correct order:", res)
            print()
        if res:
            answear+=(i+1)
    if answear:
        print("Solution for day {:} part A:".format(DAY),answear)
    if expected:
        assert answear==expected

def sort_packets(packets):
    is_sorted = False
    original = packets.copy()
    do_print=False
    while (not is_sorted):
        is_sorted = True
        sorted = []
        for i in range(0,len(packets)-1):
            if not check_order((packets[i], packets[i+1]), do_print=do_print):
                is_sorted = False
                tmp = packets[i].copy()
                packets[i] = packets[i+1]
                packets[i+1] = tmp
    return packets

def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    data = format_input(input)
    divider_packets=[[[2]], [[6]]]
    packets = divider_packets.copy()
    for pair in data:
        packets.append(pair[0])
        packets.append(pair[1])

    packets = sort_packets(packets)
    answear=1
    for i in range(len(packets)):
        if packets[i] in divider_packets: 
            answear*=(i+1)

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
        partA(input, expected=5659)
    if case == 'b' or case == 'all':
        partB(input, expected=22110)


