# Correct part1: 26400
# Correct part2: 8199963486

import os, sys

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

# print(data)

import math
def dist(v1,v2):
    d = 0
    for i in range(len(v1)):
        d+=((v1[i]-v2[i])*(v1[i]-v2[i]))
    return math.sqrt(d)

for i in range(len(data)):
    data[i] = [int(c) for c in data[i].split(',')]

distances = []
for i in range(len(data)-1):
    for j in range(i,len(data)):
        if i==j:
            continue
        d = dist(data[i], data[j])
        distances.append((d,i,j))

from operator import itemgetter
distances = sorted(distances, key=itemgetter(0))

for d in distances:
    i = d[1]
    j = d[2]
    dist=d[0]

def make_connections(connections, distances, nConnections):
    i=0
    while i<nConnections:
        dist = distances[i]
        connections[dist[1]]=connections[dist[1]]+[dist[2]]
        connections[dist[2]]=connections[dist[2]]+[dist[1]]
        i+=1
    return connections

def get_clusters(connections):
    clusters = []
    for i in range(len(connections)):
        c = connections[i]
        cluster = c
        j=0
        while j<len(cluster):
            node = cluster[j]
            cluster = cluster + connections[node]
            connections[node]=[]
            j+=1
        clusters.append(cluster)

    tmp = set()
    for c in clusters:
        c = set(c)
        str_v = ','.join(str(x) for x in c)
        if str_v!='':
            tmp.add(str_v)
    clusters = []
    for c in tmp:
        clusters.append([int(x) for x in c.split(',')])

    clusters = sorted(clusters, key=len, reverse=True)
    return clusters

def part1():
    connections = [[]]*len(data)
    connections = make_connections(connections, distances, nConnections)
    clusters = get_clusters(connections)
    answear = 1
    for i in range(3):
        answear*=len(clusters[i])
    return answear

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
            is_connected = nx.is_connected(G)
            n1 = d[1]
            n2 = d[2]
            x1 = data[n1][0]
            x2 = data[n2][0]
            return x1*x2

        i+=1

print("Solution part 1:", part1())
print("Solution part 2:", part2())


