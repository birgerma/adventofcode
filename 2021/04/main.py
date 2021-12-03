import time

import sys
import math
sys.path.append('../')

import utils.io_tools as io

data_file = './data'

def execution_time(func):
    start = time.time()
    res = func()
    end = time.time()
    print("Execution time:",end - start)
    return res
    
def test1():
    pass

def test2():
    pass

def solve1():
    # data = io.read_file_lines(data_file)
    pass


def solve2():
    # data = io.read_file_lines(data_file)
    pass


# assert test()==
# assert test2()==
# print("Test solution:",execution_time(test1))
# print("Test2 solution:",test2())


# sol1 = solve1()
# assert sol1==4147524
# print("Solution 1:", sol1)

# sol2 = solve2()
# assert sol2==3570354
# print("Solution 2:", sol2)
