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
    line = list(line)
    formated = []
    i=0
    while i<len(line):
        if(line[i]=='['):
            formated.append(line[i+1])
        else:
            formated.append('')
        i+=4
    return formated
    line = [i for i in line if (i!=']' and i!='[')]
    formated = []
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
    for line in pos:
        line = parse_line(line)
        positions.append(line)
    positions = positions[:-1]
    positions =  list(map(list, itertools.zip_longest(*positions, fillvalue=None)))
    reversed_pos = []
    for pos in positions:
        pos.reverse()
        pos = [p for p in pos if p!='']
        pos = [p for p in pos if p]
        if len(pos)>0:
            reversed_pos.append(pos)
    return reversed_pos

def parse_instructions(ins):
    instructions = []
    for line in ins:
        line = line.split(' ')
        instruction = {'n':int(line[1]), 'from':int(line[3])-1, 'to':int(line[5])-1}
        instructions.append(instruction)
    return instructions

def parse_input(input):
    pos, ins = split_positions_instructions(input.split('\n'))
    pos = parse_positions(pos)
    ins = parse_instructions(ins)
    return pos, ins

def do_move(state, fr, to, n, multimove=False):
    top_index = len(state[fr])-1
    objects = state[fr][top_index-n+1:]
    if not multimove:
        objects.reverse()
    state[fr] = state[fr][:-n]
    state[to]+=objects
    return state
    
def print_state(state):
    print("Print state:")
    for i in range(len(state)):
        print(i,":",state[i])
    print()
def simulate_movements(state, instructions, multimove=False):
    for ins in instructions:
        state = do_move(state, ins['from'], ins['to'], ins['n'], multimove=multimove)
    return state

def partA(input):
    print("Solve for day {:d} part A".format(DAY))
    pos, ins = parse_input(input)
    final_states = simulate_movements(pos, ins)
    top_crates = []
    for col in final_states:
        top_crates.append(col[-1])
    top_crate_string = "".join(top_crates)
    assert top_crate_string == "GFTNRBZPF"
    print("Top crates:", top_crate_string)

def partB(input):
    print("Solve for day {:d} part B".format(DAY))
    pos, ins = parse_input(input)
    final_states = simulate_movements(pos, ins, multimove=True)
    top_crates = []
    for col in final_states:
        top_crates.append(col[-1])
    top_crate_string = "".join(top_crates)
    assert top_crate_string == "VRQWPDSGP"
    print("Top crates:", top_crate_string)

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_file(data_file)
    partA(item_list)
    print()
    partB(item_list)

