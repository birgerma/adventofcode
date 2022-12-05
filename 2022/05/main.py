# importing sys
import sys
import os

import itertools

# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def split_positions_instructions(data_list):
    for i in range(len(data_list)):
        if data_list[i]=="":
            positions = data_list[:i]
            instructions = data_list[i+1:-1]
            return positions, instructions

def parse_line(line):
    print("Raw line:", line)
    line = list(line)
    #line = line.split("   ")
    formated = []
    i=0
    while i<len(line):
        print(line[i:i+3])
        if(line[i]=='['):
            formated.append(line[i+1])
        else:
            formated.append('')
        i+=4
    return formated
    print(formated)
    print("Splitted line:", line)
    line = [i for i in line if (i!=']' and i!='[')]
    formated = []
    print("Parse line:", line)
    for i in line:
        i=i.strip()
        if len(i)>3:
            i = i.split(" ")
            formated+=i
        else:
            formated.append(i)
    return formated

def parse_positions(pos):
    positions = []
    print("Raw pos input:")
    print_state(pos)
    for line in pos:
        line = parse_line(line)
        positions.append(line)
    for line in positions:
        print(line)
    positions = positions[:-1]
    print("Cutted positions:", positions)
    print("Zipped positions:", list(map(list, itertools.zip_longest(*positions, fillvalue=None))))
    positions =  list(map(list, itertools.zip_longest(*positions, fillvalue=None)))
    #positions = list(map(list, zip(*positions)))
    print("Unformated pos:")
    print(positions)
    reversed_pos = []
    for pos in positions:
        #reversed_pos.append(pos.reverse())
        #print("Pos line:",pos)
        pos.reverse()
        pos = [p for p in pos if p!='']
        pos = [p for p in pos if p]
        #for i in range(len(pos)):
            #print(list(pos[i])[1])
            #pos[i] = list(pos[i])[1]
        #print("Reversed:", pos)
        if len(pos)>0:
            reversed_pos.append(pos)
    #print("Formatted:", reversed_pos)
    return reversed_pos

def parse_instructions(ins):
    instructions = []
    for line in ins:
        line = line.split(' ')
        #print(line)
        instruction = {'n':int(line[1]), 'from':int(line[3])-1, 'to':int(line[5])-1}
        instructions.append(instruction)
    return instructions

def parse_input(input):
    pos, ins = split_positions_instructions(input.split('\n'))
    pos = parse_positions(pos)
    ins = parse_instructions(ins)
    return pos, ins

def do_move(state, fr, to, n, multimove=False):
    if n>0:
        #print("n>0, should to move")
        print("Should move from", fr, "to", to)
        #print("N columns:", len(state))
        print("N boxes to move:", n)
        top_index = len(state[fr])-1
        print("Top index:", top_index)
        #obj = state[fr][top_index]
        objects = state[fr][top_index-n+1:]
        print(objects)
        if not multimove:
            objects.reverse()
        print(objects)
        print(state[fr])
        state[fr] = state[fr][:-n]
        print(state[fr])
        print("To:", state[to])
        state[to]+=objects
        print("To updated:", state[to])
        return state
        quit()
        state[to].append(obj)
        #print("Updated state:", state)
        return do_move(state, fr, to, n-1)
    else:
        #print("n=0, return state:", state)
        return state
    
def print_state(state):
    print("Print state:")
    for i in range(len(state)):
        print(i,":",state[i])
    print()
def simulate_movements(state, instructions, multimove=False):
    print_state(state)
    for ins in instructions:
        state = do_move(state, ins['from'], ins['to'], ins['n'], multimove=multimove)
        print('New state:')
        print_state(state)
    return state

def partA(input):
    print("Solve for day {:d} part A".format(DAY))
    #print(input)
    pos, ins = parse_input(input)
    #print(pos)
    #print(ins)
    print("Original state:")
    print_state(pos)
    #quit()
    final_states = simulate_movements(pos, ins)
    top_crates = []
    for col in final_states:
        top_crates.append(col[-1])
    top_crate_string = "".join(top_crates)
    assert top_crate_string == "GFTNRBZPF"
    print(top_crate_string)

def partB(input):
    print("Solve for day {:d} part B".format(DAY))
    pos, ins = parse_input(input)
    #print(pos)
    #print(ins)
    print("Original state:")
    print_state(pos)
    #quit()
    final_states = simulate_movements(pos, ins, multimove=True)
    top_crates = []
    for col in final_states:
        top_crates.append(col[-1])
    top_crate_string = "".join(top_crates)
    assert top_crate_string == "VRQWPDSGP"
    print(top_crate_string)

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_file(data_file)
    partA(item_list)
    partB(item_list)

