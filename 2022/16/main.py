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

import igraph as graph
def format_input(input):
    data = {}
    for line in input:
        line = line.split(" ")
        name = line[1]
        flow = int("".join(list(line[4].split("=")[1])[:-1]))
        nodes = "".join(line[9:]).split(",")
        data[name]=[flow, nodes]

    # Create graph of nodes:
    vmap = {}
    index = 0
    for node in data:
        vmap[index]=node
        vmap[node]=index
        index+=1
    
    g = graph.Graph(directed=True)
    g.add_vertices(len(data))
    for node in data:
        connections = data[node][1]
        i1 = vmap[node]
        for con in connections:
            i2 = vmap[con]
            g.add_edges([(i1,i2)])


    non_zero_nodes = [node for node in data.keys() if data[node][0]>0]
    # Compute shortest path
    path = {}
    for n1 in non_zero_nodes:
        for n2 in non_zero_nodes:
            if n1!=n2:
                p=g.get_shortest_paths(vmap[n1],to=vmap[n2],mode=graph.OUT,output='vpath')
                path[(n1,n2)]=p[0]
        # Compute shortest path from AA to all nodes
        p=g.get_shortest_paths(vmap['AA'],to=vmap[n1],mode=graph.OUT,output='vpath')
        path[('AA', n1)] = p[0]


    return data, path, vmap


MEM = {}
n_computations = 0
import math
max_comp = math.factorial(10)
import time
from collections import deque

def compute_total_flow(t, data):
    flow = [0]*30
    s = 0
    #print("Compute score")
    for i in range(len(flow)):
        if i<len(t):
            move = t[i]
            #print("Move:", move)
            if move in data:
                #print("Is flow:", data[move][0])
                s+=data[move][0]
        flow[i]=s
   #print(flow)
    return sum(flow)
def find_best_path(data, path, vmap):

    max_t=30
    Q = deque()
    closed_nodes = [node for node in data if data[node][0]>0]
    state = ('AA',['AA'], closed_nodes)
    Q.append(state)

    SEEN = set()
    best_score = 0
    best_path = []

    while Q:
        #print(len(Q))
        node, t, closed = Q.pop()
        if len(t)>30:
            t=t[:30]

        if str(t) in SEEN:
            #print("Already seen")
            continue
        SEEN.add(str(t))
        if len(t)>=30 or len(closed)==0:
            #print("Final t:", t)
            score = compute_total_flow(t, data)
            #print("Final score:", score)
            if score>best_score:
                print("New best score:", score)
                best_score = score
                best_path = t
            #else:
            #    print("Compare:")
            #    for i in range(30):
            #        print(t[i], best_path[i], t[i]==best_path[i])
            #    print(str(t), str(best_path))
            #    print(",".join(t)==",".join(best_path))
            #    quit()
        #print("State:", node, t, closed)
        flow = data[node][0]
        #print("Potential flow:", flow)


        if flow>0 and node in closed:
            #print("Can open, should be implemented")
            #print("Closed:", closed)
            new_closed = closed.copy()
            new_closed.remove(node)
            #print("New closed",new_closed)
            new_state = (node, t+[node], new_closed)
            t=t+[node]
            closed = new_closed
            #print("New state:", new_state)
            #Q.append(new_state)
            if len(closed)==0:
                Q.append(new_state)
        
        # Try to move to nodes
        for n in closed:
            if n!=node:
                p = path[(node,n)]
                moves = []
                for i in range(len(p)-1):
                    moves.append(vmap[p[i]]+'->'+vmap[p[i+1]])

                next_node = n
                #print("Closed nodes:", closed)
                new_state = (n, t+moves, closed)
                Q.append(new_state)
    print("Done with simulation")
    compute_total_flow(best_path, data)
    print("Best t:", best_path)
    print("Best score:", best_score)

def partA(input, expected=None):
    print("Solve for day {:} part A".format(DAY))
    data, path, vmap = format_input(input)
    init = 'AA'
    start_time = time.time()

    # Compute flow addition by going from current node to any other closed node:
    closed_nodes = [node for node in data if data[node][0]>0]

    find_best_path(data, path, vmap)

    quit()
    current = init
    t=0
    max_t=30
    for n in closed_nodes:
        p = path[(current, n)]
        dist = len(p)-1
        print("Dist", current,'->', n,":", dist)
        flow = data[n][0]
        print("Added flow:", flow)
        factor = (max_t-t)-1-dist
        addition = factor*flow
        print("Total addition:", addition)
        print("Time factor:", factor)
        print()
    print("commputation time:", time.time()-start_time)
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
        partA(input, expected=1584)
    if case == 'b' or case == 'all':
        partB(input)


