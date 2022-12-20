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
def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    original = {}
    prev = None
    head = None
    og_index=0
    zero_node = None
    
    for d in data:
        node = Node(d)
        if d==0:
            zero_node = node
        original[og_index]=node
        og_index+=1
        if prev:
            prev.insert_after(node)
        else:
            head=node
        prev = node
    tail = node
    n_numbers = len(original.keys())

    if len(original.keys())<10:
        print("original list:")
        print_ll(head)
    print()
    for og_index in original:
        node = original[og_index]
        sign = 1 if node.data>=0 else -1
        steps = abs(node.data)%n_numbers
        steps*=sign
        print("Abs node:", abs(node.data))
        print("Step conversion:", node.data, steps)
        print("Move node", node, steps,'steps')
        if steps>0:
            wrap = head
        else:
            wrap = tail

        if steps>0:
            n = node.next if node.next else wrap
            tmp = node.prev
            node.disconnect()
            if n.prev is None:
                head = n
            if n.next is None:
                tail = n
            while steps>1:
                if n.next is not None:
                    n = n.next
                else: # Wrap around
                    n=wrap
                steps-=1
           # if n==tail:
           #     head.insert_before(node)
           #     head=node
           # else:
           #     n.insert_after(node)
            n.insert_after(node)
        elif steps<0:
            n = node.prev if node.prev else wrap
            node.disconnect()
            if n.prev is None:
                head = n
            if n.next is None:
                tail = n
            while steps<-1:
                if n.prev is not None:
                    n = n.prev
                else:
                    n = wrap
                steps+=1
          #  if n==head:
          #      tail.insert_after(node)
          #      tail=node
          #  else:
          #      n.insert_before(node)
            n.insert_before(node)
        else:
            pass # 0 do not move
        if node.prev is None:
            head = node
        if node.next is None:
            tail = node
        if len(original.keys())<10:
            print_ll(head)
            print()
    
    if len(original.keys())<10:
        print_ll(head)
    groove_numbers = [s%n_numbers for s in [1000, 2000, 3000]]
    print("Orig groove:", groove_numbers)
    print("1000%1=",1000%1)
    groove_numbers.sort()
    print("Len:", n_numbers)
    print("Groove:", groove_numbers)
    print("Zero:", zero_node)
    j=0
    node = zero_node
    answear = 0
    for i in groove_numbers:
        while j<i:
            node = node.next if node.next else head
            j+=1
        print("Final node:", node)
        answear+=node.data

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
        partA(input)
    if case == 'b' or case == 'all':
        partB(input)


