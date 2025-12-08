# Correct part1: 26400
# Correct part2: 8199963486

import os, sys
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
# print(data)

distances = []
for i in range(len(data)-1):
    for j in range(i,len(data)):
        if i==j:
            continue
        d = dist(data[i], data[j])
        # print(d, data[i], data[j])
        distances.append((d,i,j))
    # break

from operator import itemgetter
# print('Unsorted:', distances)
distances = sorted(distances, key=itemgetter(0))
# print()
# print('Sorted:', distances)
for d in distances:
    i = d[1]
    j = d[2]
    dist=d[0]
    # print(dist, data[i], data[j])

# print('Init connections:', connections)
# print(len(data))
def make_connections(connections, distances, nConnections):
    i=0
    while i<nConnections:
        # print('Connection number:', i)
        # print('Connecting:', distances[i])
        # print(data[distances[i][1]], '<->', data[distances[i][2]])
        dist = distances[i]
        # print('dist:', dist)
        # print(dist[1], dist[2])
        # print(connections[dist[1]]+[dist[2]])
        connections[dist[1]]=connections[dist[1]]+[dist[2]]
        connections[dist[2]]=connections[dist[2]]+[dist[1]]
        # connections[dist[2]].append(dist[1]) 
        # print('Current connections:', connections)
        # print(i)
        i+=1
        # print('----')
        # exit(0)
    return connections

# print('Connections:', connections)

# print('Find clusters')
def get_clusters(connections):
    clusters = []
    for i in range(len(connections)):
        # print(len(set(c)),set(c))
        c = connections[i]
        # print(i,':',len(c),c)
        cluster = c
        j=0
        while j<len(cluster):
        # for node in c:
            node = cluster[j]
            # print('node:', node)
            cluster = cluster + connections[node]
            connections[node]=[]
            j+=1
        clusters.append(cluster)

    tmp = set()
    for c in clusters:
        # print(c)
        c = set(c)
        str_v = ','.join(str(x) for x in c)
        if str_v!='':
            tmp.add(str_v)
        # tmp.add[','.join(str(x) for x in c)]
    clusters = []
    for c in tmp:
        clusters.append([int(x) for x in c.split(',')])

    # print('Unsorted:', clusters)
    clusters = sorted(clusters, key=len, reverse=True)
    return clusters
    # print('Sorted:')
    # for c in clusters:
    #     print(c)
    # print('-----')
    # print(tmp)


def part1():
    connections = [[]]*len(data)
    connections = make_connections(connections, distances, nConnections)
    clusters = get_clusters(connections)
    answear = 1
    for i in range(3):
        # print(len(clusters[i]))
        answear*=len(clusters[i])
    return answear

def part2():
    connections = [[]]*len(data)
    i=0
    start = 5100
    while True:
        # print(distances)
        # print()
        # print(distances[i:])
        # exit(0)
        connections = make_connections(connections, distances[i:], start)
        if start>1:
            i=start
        start = 1

        # print(connections)
        clusters = get_clusters(connections.copy())
        # print(clusters)
        print(i,len(clusters[0]))
        # print(len(data))
        # print()
        if len(clusters[0])==len(data):
            print('Done')
            print('Last connection:', distances[i])
            v1 = data[distances[i][1]]
            v2 = data[distances[i][2]]
            return v1[0]*v2[0]
            exit(0)
        i+=1
        # if i>1:
        #     exit(0)
        # exit(0)

    # answear = 1
    # for i in range(3):
    #     # print(len(clusters[i]))
    #     answear*=len(clusters[i])
    # return answear
# print("Solution part 1:", part1())
print("Solution part 2:", part2())


