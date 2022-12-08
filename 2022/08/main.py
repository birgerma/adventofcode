# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def format_input(input):
    formated = []
    for i in input:
        i = [int(x) for x in list(i)]
        formated.append(i)
    return formated

def print_matrix(mat):
    for row in mat: print(row)
    print()

def print_visible(visible, xrange, yrange):
    for y in yrange:
        for x in xrange:
            value = True
            if (y,x) in visible:
                value = visible[(y,x)]
            print(value," ", end="")
        print()

def find_visible_trees(array):
    is_visible = [True]*len(array)
    max_height = array[0]
    for x in range(1,len(array)-1):
        #print("x=",x,"array[x]=",array[x],'max_x=', max_height)
        if array[x]<=max_height:
            is_visible[x]=False
        max_height = array[x] if array[x]>max_height else max_height
    return is_visible

def or_list(a,b):
    lst = []
    for i in range(len(a)):
        lst.append(a[i] or b[i])
    return lst

def find_visible_cols(data, res_mat={}, reverse=False):
    is_visible = []
    is_visible.append([True]*len(data[0]))
    #print(is_visible)
    for row in range(1,len(data)-1):
        left_visible = find_visible_trees(data[row])
        right_visible = find_visible_trees(data[row][::-1])[::-1]
        visible_row = or_list(left_visible, right_visible)
        is_visible.append(visible_row)
        #print(data[row])
        #print(left_visible)
        #print(right_visible)
        #print(visible_row)
        #quit()

        #print(data[row][::-1])
    is_visible.append([True]*len(data[0]))
    for row in is_visible:
        print(row)
    return is_visible

import numpy as np
def transpose(mat):
    return np.array(mat).T.tolist()

def find_visible(data):
    print_list(data)
    print()
    transposed = np.array(data).T.tolist()
    print_list(transposed)

    visible_a = find_visible_cols(data)
    visible_b = transpose(find_visible_cols(transpose(data)))
    is_visible = []
    for i in range(len(visible_a)):
        is_visible.append(or_list(visible_a[i], visible_b[i]))

    return is_visible
#right_visible = find_visible_trees(data[row].reverse()).reverse()
    #test_array = data[1]
    #print(test_array)
    #visible = find_visible_trees(test_array)

def partA(input, expected=None):
    print("Solve for day {:d} part A".format(DAY))
    data = format_input(input)
    result = find_visible(data)
    
    n_visible = 0
    for row in result:
        count = np.count_nonzero(row)
        n_visible+=count
    print(n_visible)
    #print_visible(result, range(0,len(data[0])),range(0,len(data)))
    answear = n_visible
    if expected:
        assert answear==expected

def find_look_range_right(data, x0,y0):
    score = 0
    y=y0
    height=data[y0][x0]
    for x in range(x0+1, len(data[0])):
        score+=1
        if data[y][x]>=height:
            break
    return score

def find_look_range_left(data, x0,y0):
    score = 0
    y=y0
    height=data[y0][x0]
    for x in range(x0-1, -1, -1):
        score+=1
        if data[y][x]>=height:
            break
    return score

def find_look_range_up(data, x0, y0):
    score = 0
    x=x0
    height = data[y0][x0]
    for y in range(y0-1, -1,-1):
        score+=1
        if data[y][x]>=height:
            break
    return score

def find_look_range_down(data,x0,y0):
    score = 0
    x=x0
    height=data[y0][x0]
    for y in range(y0+1, len(data)):
        score+=1
        #print("Down score: y=", y)
        if data[y][x]>=height:
            break
    return score

def find_scenic_score(data, x0,y0):
    # Find score to the right:
    right = find_look_range_right(data, x0, y0)
    left = find_look_range_left(data, x0, y0)
    up = find_look_range_up(data, x0, y0)
    down = find_look_range_down(data, x0, y0)
    #print("y=", y0, "x=", x0, "Right score=",right)
    #print("y=", y0, "x=", x0, "Left score=",left)
    #print("y=", y0, "x=", x0, "Up score=",up)
    #print("y=", y0, "x=", x0, "Down score=",down)
    return right*left*up*down

def find_scenic_scores(data):
    print_list(data)
    #result = [[0]*len(data[0])]*len(data)
    result = {}
    for y in range(1,len(data)-1):
        for x in range(1,len(data[0])-1):
            #y=1
            #x=2
            score = find_scenic_score(data,x,y)
            result[(y,x)]=score
            print("x=",x, "y=",y,"score=", score)
            #quit()

            #print(data[y][x]," ", end="")
        #print()
    print_list(result.values())
    return result
def partB(input, expected=None):
    print("Solve for day {:d} part B".format(DAY))
    data = format_input(input)
    scores = find_scenic_scores(data)
    answear = max(scores.values())
    print("Answear:", answear)
    if expected:
        assert answear==expected

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    #partA(item_list, expected=1854)
    partB(item_list, expected=527340)


