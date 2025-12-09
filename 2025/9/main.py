# Correct part1: 4725826296
# Correct part2: 

# Too low: 316303830
#          2447025923

import os, sys
sys.path.append('..')

from lib.io import read_file

fname = 'test'
fname = 'data'
data = read_file(fname)

def compute_area(p1, p2):
    print(p1,p2)
    return (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)

for i in range(len(data)):
    data[i] = [int(x) for x in data[i].split(',')]

# print(data)
import math
# topLeft = data[0]
# topRight = data[0] 
# bottomLeft = data[0]
# bottomRight = data[0]

from operator import itemgetter
xsort = sorted(data, key=itemgetter(0))
ysort = sorted(data, key=itemgetter(1))

minX = [xsort[0]]
i=1
while xsort[i][0]==xsort[i-1][0]:
    minX.append(xsort[i])
    i+=1
maxX = [xsort[-1]]
i=-2
while xsort[i][0]==xsort[i-1][0]:
    maxX.append(xsort[i])
    i-=1

minY = [ysort[0]]
i=1
while ysort[i][0]==ysort[i-1][0]:
    minY.append(ysort[i])
    i+=1
maxY = [ysort[-1]]
i=-2
while ysort[i][0]==ysort[i-1][0]:
    maxY.append(ysort[i])
    i-=1

ref = 2447025923
# Brute force:
area = 0
for i in range(len(data)-1):
    for j in range(i+1, len(data)):
        a = compute_area(data[i], data[j])
        if a>area:
            area = a
        if area>ref:
            print("Found new case:", data[i], data[j])
            print('Area:', area)

print(minX)
print(maxX)
print(minY)
print(maxY)
exit(0)
minv = minX+maxX+minY+maxY


print(minv)
area = 0
for i in range(len(minv)-1):
    for j in range(i+1,len(minv)):
        print(minv[i], minv[j])
        a = compute_area(minv[i], minv[j])
        print(a)
        if a > area:
            area = a
print('Max area:', area)
exit(0)

# minX = xsort[:2]
# maxX = xsort[-2:]
# print(minX)
# if minX[0][1]<minX[1][1]:
#     topLeft=minX[0]
#     bottomLeft=minX[1]
# else:
#     topLeft=minX[1]
#     bottomLeft=minX[0]
# if maxX[0][1]<maxX[1][1]:
#     topRight = maxX[0]
#     bottomRight = maxX[1]
# else:
#     topRight = maxX[1]
#     bottomRight = maxX[0]
#
#
# print(topLeft)
# print(topRight)
# print(bottomLeft)
# print(bottomRight)
# print(maxX)

# for p in data:
#     if p[0]<bottomLeft[0]:
#         bottomLeft=p
#     elif p[0]<=bottomLeft[0] and p[1]>=bottomLeft[1]:
#         bottomLeft=p
#     elif p[0]>=bottomRight[0] and p[1]>=bottomRight[1]:
#         bottomRight = p
#     if p[0]<=topLeft[0] and p[1]<=topLeft[1]:
#         topLeft=p
#     elif p[0]>=topRight[0] and p[1]<=topRight[1]:
#         topRight=p


# print(topLeft, topRight, bottomLeft, bottomRight)
# print("TopLeft", topLeft)
      # , topRight, bottomLeft, bottomRight)

# area = compute_area(minX, maxX)
area = max([compute_area(bottomLeft,topRight), compute_area(topLeft, bottomRight)])
#
# print(minY)
print(area)
print(compute_area(bottomLeft, topRight))
#
