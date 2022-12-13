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
    #print("Parse string:", string, "start=", start)
    i=start
    while i<len(string):
    #for i in range(start,len(string)):
        c = string[i]
        #print(string)
        #print("c:", c, "i:",i)
        i+=1
        if c==',':
            #print("Next num:", str_num)
            if str_num!="":
                lst.append(int(str_num))
            str_num=""
            #print("New list:", lst)
        elif c=='[':
            #print("New nested list")
            nested, new_i = parse(string, start=i)
            #print("Current list:", lst)
            #print("Nested list:", nested, "i=", new_i)
            lst.append(nested)
            #print("New list:", lst)
            i=new_i
            #quit()
        elif c==']':
            #print("End of list")
            if str_num!="":
                lst.append(int(str_num))
            break
            #quit()
        else:
            str_num+=c
    
    #print("Returning on i=", i)
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
        #print("Pair:", i+1)
        #print("Original:", pair)
        #print("Left:", left)
        #print("Right:", right)
        #print()
        formated.append((left,right))
        #quit() 
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
                print("Different types, converting")
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
                    print("Is same, continue")
            elif isinstance(l, list) and isinstance(r,list):
                res = check_order((l,r),do_print, tab_level+'\t')
                if not res:
                    return False
                else: # Do some extra checking
                    print("Extra check")
                    if len(l)==len(r):
                        if l==[] and r==[]:
                            print("Both empty, continue check")
                            pass # Continue checking
                        elif l[-1]==r[-1]:
                            print("Same len, or same values, continue")
                            pass
                        else:
                            return True
                            print(l, r)
                            quit()
                    else:
                        print("Extra check also returned True")
                        return True
            else:
                print("Should not be here!")
                Exception()
                quit()
                l = [l] if isinstance(l,int) else l
                r = [r] if isinstance(r,int) else r
                return check_order((l,r),do_print, tab_level+'\t')
                if res:
                    return True
                    pass
                else:
                    return False

        else:
            if do_print:
                print(tab_level, "- Right side ran out of items, so inputs are not in the right order")
            return False

    if do_print:
        print(tab_level, " - Left side ran out of items, so inputs are in the right order")
    return True
            
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    do_print=True
    answear = 0
    for i in range(len(data)):
        pair = data[i]
        print("== Pair", i+1, "==")
        res = check_order(pair,do_print=do_print)
        print("Is in correct order:", res)
        print()
        if res:
            answear+=(i+1)
# 679 is too low    
# 6118 is too high
# 4751 is too low
    if answear:
        print("Solution for day {:} part A:".format(DAY),answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:} part B".format(DAY))
    data = format_input(input)

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
        partA(input, expected=5659)
    if case == 'b' or case == 'all':
        partB(input)


