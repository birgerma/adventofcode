# Correct part1: 26400
# Correct part2: 8199963486

import os, sys
import math

from operator import itemgetter
import networkx as nx

sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
if fname=='test':
    nConnections = 10
elif fname=='data':
    nConnections = 1000

data = read_file(fname)
for i in range(len(data)):
    data[i] = [int(c) for c in data[i].split(',')]

def dist(v1,v2):
    d = 0
    for i in range(len(v1)):
        d+=((v1[i]-v2[i])*(v1[i]-v2[i]))
    return math.sqrt(d)


distances = []
for i in range(len(data)-1):
    for j in range(i,len(data)):
        if i==j:
            continue
        d = dist(data[i], data[j])
        distances.append((d,i,j))

distances = sorted(distances, key=itemgetter(0))

def part1():
    G = nx.Graph()
    added_nodes = set()
    i = 0
    while i<nConnections:
        d = distances[i]
        G.add_edges_from([(d[1],d[2])])
        i+=1
    components = list(nx.connected_components(G))
    subgraphs = [G.subgraph(c).copy() for c in components]
    clusters = []
    for g in subgraphs:
        clusters.append(len(g.nodes))
    clusters = sorted(clusters, reverse=True)
    return clusters[0]*clusters[1]*clusters[2]

def part2():
    G = nx.Graph()
    added_nodes = set()
    i = 0
    while i<len(distances):
        d = distances[i]
        G.add_edges_from([(d[1],d[2])])
        if len(added_nodes)<len(data):
            added_nodes.add(d[1])
            added_nodes.add(d[2])
        if len(added_nodes)==len(data) and nx.is_connected(G):
            return data[d[1]][0]*data[d[2]][0]

        i+=1

print("Solution part 1:", part1())
print("Solution part 2:", part2())


