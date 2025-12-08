# Correct part1: 26400
# Correct part2: 

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

connections = [[]]*len(data)
# print('Init connections:', connections)
# print(len(data))
i=0
while i<nConnections:
    print('Connection number:', i)
    print('Connecting:', distances[i])
    print(data[distances[i][1]], '<->', data[distances[i][2]])
    dist = distances[i]
    print('dist:', dist)
    print(dist[1], dist[2])
    print(connections[dist[1]]+[dist[2]])
    connections[dist[1]]=connections[dist[1]]+[dist[2]]
    connections[dist[2]]=connections[dist[2]]+[dist[1]]
    # connections[dist[2]].append(dist[1]) 
    # print('Current connections:', connections)
    # print(i)
    i+=1
    print('----')
    # exit(0)

# print('Connections:', connections)

# print('Find clusters')
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
        print('node:', node)
        cluster = cluster + connections[node]
        connections[node]=[]
        j+=1
    clusters.append(cluster)

tmp = set()
for c in clusters:
    print(c)
    c = set(c)
    str_v = ','.join(str(x) for x in c)
    if str_v!='':
        tmp.add(str_v)
    # tmp.add[','.join(str(x) for x in c)]
clusters = []
for c in tmp:
    clusters.append(c.split(','))

# print('Unsorted:', clusters)
clusters = sorted(clusters, key=len, reverse=True)
print('Sorted:')
for c in clusters:
    print(c)
# print('-----')
# print(tmp)

answear = 1
for i in range(3):
    print(len(clusters[i]))
    answear*=len(clusters[i])

print(answear)
