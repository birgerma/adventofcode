# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

def format_input(input):
    input = [int(i) for i in input]
    return input

class Node:

    def __init__(self, data):
        self.data=data
        self.prev = None
        self.next = None

    def verbose(self):
        left = str(self.prev) if self.prev else "HEAD"
        right = str(self.next) if self.next else "TAIL"
        return left + " -> " + str(self.data) + " -> " + right

    def set_prev(self, node):
        self.prev=node
    
    def set_next(self, node):
        self.next=node

    def insert_after(self, node):
        right = self.next.data if self.next else "TAIL"
        tmp_node = self.next
        self.next = node
        node.set_prev(self)
        node.set_next(tmp_node)

        if tmp_node is not None:
            tmp_node.set_prev(node)

    def insert_before(self, node):
        tmp_node = self.prev
        self.prev = node

        node.set_next(self)
        node.set_prev(tmp_node)
        
        if tmp_node is not None:
            tmp_node.set_next(node)

    def disconnect(self):
        if self.prev is not None:
            self.prev.set_next(self.next)
        if self.next is not None:
            self.next.set_prev(self.prev)
        self.prev=None
        self.next=None

    def __repr__(self):
        return str(self.data)


def print_ll(node):
    while node is not None:
        print(node, end='')
        node=node.next
        if node is not None:
            print('-> ', end='')
    print()

from llist import dllist, dllistnode
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    original = {}
    prev = None
    head = None
    og_index=0
    zero_node = None
    
    lst = dllist()
    for d in data:
        node = dllistnode(d)
        if d==0:
            zero_node = node
        original[og_index]=node
        og_index+=1
        lst.insertnode(node)

    n_numbers = len(original.keys())

    wraparound =False
    if lst.size<10: print('Init:', lst)
    for og_index in original:
        node = original[og_index]
        steps = node.value
        n_steps = abs(steps)-1
        #sign = -1 if steps<0 else 1
        #steps = steps%lst.size
        #steps = steps*sign
        
        #n = node
        if steps>0:
            n = node.next if node.next else lst.first
            lst.remove(node)
            #while steps>0:
            for step in range(steps-1):
              if n.next:
                n=n.next
                #steps-=1
              else:
                n = lst.first
            #v = lst.remove(node)
            lst.insertnodeafter(node,n)
            #print("Insert", node.value,"after", n.value)
        elif steps<0:
            n = node.prev if node.prev else lst.last
            lst.remove(node)
            #while steps<1:
            for step in range(abs(steps)-1):
              if n.prev:
                n = n.prev
                #steps+=1
              else: 
                n=lst.last
                wraparound=True
                #steps+=1
            print("Node:", node)
            print("n=", n)
            #lst.remove(node)
            lst.insertnodebefore(node, n)
        else:
            pass # 0 do not move
        prev = node.prev if node.prev else lst.last
        nxt = node.next if node.next else lst.first
        print(node.value,"moves between",prev.value,"and", nxt.value)
        if lst.size<10: print('List:', lst,'\n')
        #quit()

    groove_numbers = [1000, 2000, 3000]
    print("Orig groove:", groove_numbers)
    #groove_numbers = [s%n_numbers for s in groove_numeers
    groove_numbers.sort()
    print("Len:", n_numbers)
    print("Groove:", groove_numbers)
    print("Zero:", zero_node)
    j=0
    node = zero_node
    answear = 0
    for i in groove_numbers:
        while j<i:
            node = node.next if node.next else lst.first
            j+=1
        print("Final node:", node, node.value)
        answear+=node.value
        print(answear)
    print("Answear:",answear)
# -928?
# 928 wrong
# 4073 is wrong
# 9476 too high
# 12971 is too high
# 13611 probably too high
# 18506 probably too high
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
        partA(input, expected=4066)
    if case == 'b' or case == 'all':
        partB(input)


