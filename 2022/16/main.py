# importing sys
import sys
import os
 
import argparse
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = os.getcwd().split('/')[-1]

DEBUG = True

def dprint(*args):
    if DEBUG:
        print(args)

def format_input(input):
    data = {}
    for line in input:
        line = line.split(" ")
        name = line[1]
        flow = int("".join(list(line[4].split("=")[1])[:-1]))
        nodes = "".join(line[9:]).split(",")
        data[name]=[flow, nodes]
    return data

def compute_flow(t, cave_map):
    if len(t)>30:
        print("Flow error")
        quit()
    score = [0]
    s=0
    for move in t:
        if move in cave_map.keys():
            s+=cave_map[move][0]
            #s = score[-1]
        score.append(s)
    return score[0:30]

def has_cycle(path):
    #print("Original path:", path)
    rev = path[::-1]
    #print("Reverse path:", rev)

    visited = []
    for p in rev:
        if not p.startswith("move->"):
            # No cycle if opening something
            return False
        elif p in visited:
            # Found cycle
            #print("Found cycle")
            return True
        visited.append(p)
    return False
    if len(path)>8:
        quit()
    return False
import time
def is_all_opened(t, cave_map):
    for node in cave_map.keys():
        if cave_map[node][0]>0:
            if node not in t:
                return False
    return True

MEM = {}
n_computations = 0
import math
max_comp = math.factorial(10)
def find_max_flow(node, t, cave_map, n_visited, n_to_visit):
    global n_computations, MEM
    n_computations+=1
    sleep = 5
    t_max = 30
    #if len(t)>=t_max or is_all_opened(t, cave_map) or has_cycle(t):
    if len(t)>=t_max or n_visited==n_to_visit or has_cycle(t):
        t_str = "".join(t)
        while len(t)<t_max:
            t.append("-")
        score = sum(compute_flow(t, cave_map))
        MEM[t_str]=score
        return score

    key = "".join(t)
    if key in MEM:
        return MEM[key]

    flow = cave_map[node][0]
    nodes = cave_map[node][1]
    DEBUG=False
    if DEBUG:
        dprint("Current:", node)
        dprint("Flow:", flow)
        dprint("Nodes:", nodes)
        dprint("Time:", t)
        dprint("Flow>0", flow>0)
        dprint("node is open:", node in t)
        dprint("")
    if DEBUG:
        time.sleep(sleep)
    #if is_all_opened(t, cave_map) or has_cycle(t):
    #if is_all_opened(t, cave_map):
    #    print("ERROR")
    #    quit()
    #    #print("All nodes opened, compute final score")
    #    #t_str = "".join(t)
    #    diff = t_max-len(t)
    #    t+=["-"]*diff
    #    #while len(t)<t_max:
    #    #    t.append("-")
    #    MEM[key]=t
    #    return t

    #if "".join(t) in MEM.keys():
    #    return MEM["".join(t)]

    max_score = 0
    if flow>0 and node not in t:
        # Open node flow
        t_tmp = t+[node]
        next_node = node
        max_score = find_max_flow(next_node, t_tmp, cave_map, n_visited+1, n_to_visit)

    for n in nodes:
        move_str = "move->"+n
        #t_tmp = t + [move_str]
        score = find_max_flow(n, t+[move_str], cave_map, n_visited, n_to_visit)
        if score>max_score:
            max_score = score
            #print("Best score:", max_score)
        MEM[key]=max_score
    return max_score

def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data = format_input(input)
    init = 'AA'
    to_visit = []
    for node in data:
        print(data[node])
        if data[node][0]>0:
            to_visit.append(node)
    print(to_visit)
    start_time = time.time()
    max_flow = find_max_flow(init, [], data, 0, len(to_visit))
    print(max_flow)
    print("commputation time:", time.time()-start_time)
    assert max_flow==1651
    quit()
    flow = compute_flow(moves, data)
    open_valves = []
    for i in range(len(moves)):
        print("=== Minute", i+1, "===")
        move=moves[i]
        f=flow[i]
        if len(open_valves)>0:
            print("Valve", open_valves, "are open")
        else:
            print("No valves are open")
        if move in data.keys():
            open_valves.append(move)
            print("Open",move," ", end='')
        else:
            print(move,end='')
        print(" current flow:", f)
        print()
    answear = None
    #f = compute_flow(flow,data)
    print("Final flow:", flow)
    print("Total score:", sum(flow))

    print(len(moves))
    print(len(flow))
    test = [20,
20,
20,
33,
33,
33,
33,
54,
54,
54,
54,
54,
54,
54,
54,
76,
76,
76,
76,
79,
79,
79,
81,
81,
81,
81,
81,
81]
    #print(test)
    #print(sum(test))
    s1=0
    s2=0
    for i in range(len(test)):
        print(flow[i], test[i])
        s1+=flow[i]
        s2+=test[i]
    print(s1,s2)
    quit()
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


