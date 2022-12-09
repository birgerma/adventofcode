# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def format_input(input):
    instructions = []
    for line in input:
        ins = line.split(" ")
        ins[1] = int(ins[1])
        instructions.append(ins)
    return instructions

def abs(x):
    if x<0:
        return -x
    return x

def is_too_far(p1, p2):
    return abs(p1[0]-p2[0])>1 or abs(p1[1]-p2[1])>1

def normalize(x):
    if x!=0:
        return x//abs(x)
    return 0

def get_direction(p1, p2):
    dirX = normalize(p1[0]-p2[0])
    dirY = normalize(p1[1]-p2[1])
    return dirX, dirY
def move_head(ins, head, tails):
    #print(ins, head)
    #print("Print current tails:")
    #for i in range(len(tails)):
    #    print(tails[i])
    #    print()
    dir = ins[0]
    step = ins[1]
    if step>0:
        head_pos = head[-1]
        #print("Init head pos:", head_pos)
        #print("Init ins:", ins)
        if dir=='U':
            head_pos = (head_pos[0], head_pos[1]-1)
        elif dir=='D':
            head_pos = (head_pos[0], head_pos[1]+1)
        elif dir=='L':
            head_pos = (head_pos[0]-1, head_pos[1])
        elif dir=='R':
            head_pos = (head_pos[0]+1, head_pos[1])
        #print("New head pos:", head_pos)
        ins[1] = ins[1]-1
        #print("New ins:", ins)
        head.append(head_pos)
        new_tails = []
        tail_moved=False
        for i in range(len(tails)):
            tail = tails[i].copy()
            #print("Moving tail:", i+1)
            #print("Using head_pos=", head_pos)
            #print("Tail len:", len(tail))
            #print("Tail:", tail)
            #print("All tails:", tails)
            tail_pos = tail[-1]
            #print("Init tail pos:", tail_pos)
            if is_too_far(head_pos, tail_pos):
                #print("Need to move",i)
                #print("Init tail pos:", tail_pos)
                dirX, dirY = get_direction(head_pos, tail_pos)
                tail_pos = (tail_pos[0]+dirX, tail_pos[1]+dirY)
                #print("Need to move tail!")
                #print("Move direction:", dirX, dirY)
                #print("New tail pos:", tail_pos)
                #print("Is still too far?:", is_too_far(head_pos,tail_pos))
                tail.append(tail_pos)
                tail_moved = True
            else:
                pass
                #print("Do not need to move", i+1)
                #tail.append(tail[-1])
            #print("New tail position:", tail[-1])
            head_pos = tail[-1]
            new_tails.append(tail)
            #print("Old tails:", tails)
            #print("New tails:", new_tails)
        #print("Head:", head[-1], "Tail:",tail[-1])
        #print("Print current tail positions:")
        #print_tail_pos(new_tails)
        if tail_moved:
            pass
            #quit()
        return move_head(ins, head, new_tails)
    else:
        return head, tails

def make_instructions(ins, head, tails):
    for i in ins:
        head,tails = move_head(i, head, tails)
    return head, tails

def partA(input, expected=None):
    print("Solve for day {:d} part A".format(DAY))
    instructions = format_input(input)
    head, tails = make_instructions(instructions, [(0,0)], [[(0,0)]])
    tail = tails[0]
    print_list(tail)
    unique_tail_pos = set(tail)
    answear = len(unique_tail_pos)
    print("Result:", answear)
    if expected:
        assert answear==expected

def print_tail_pos(tails):
    for tail in tails:
        print(tail[-1])

def partB(input, expected=None):
    print("Solve for day {:d} part B".format(DAY))
    instructions = format_input(input)
    tails = [[(0,0)]]*9
    print("Original tails:", tails)
    for tail in tails:
        print(tail)
    head, tails = make_instructions(instructions, [(0,0)], tails)
    print_tail_pos(tails)
    tail = tails[8]
    print_list(tail)
    unique_tail_pos = set(tail)
    answear = len(unique_tail_pos)
    print("Result:", answear)
    if expected:
        assert answear==expected

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    #partA(item_list, expected=5883)
    partB(item_list,expected=2367)

