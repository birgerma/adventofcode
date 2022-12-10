# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

class ComputeSystem:

    def __init__(self, instructions):
        self.instructions = instructions
        self.x = [1]

    def run(self):
        for ins in self.instructions:
            x = self.x[-1]
            if ins[0]=='addx':
                self.x.append(x) # Clock cycle 1
                x+=ins[1]
                self.x.append(x)
                print("New x:", self.x)
            elif ins[0]=='noop':
                self.x.append(x)
    def getx(self):
        return self.x

def format_input(input):
    data = []
    for i in input:
        i = i.split(" ")
        if len(i)>1:
            i[1]=int(i[1])
        data.append(i)
    return data

def partA(input, expected=None):
    print("Solve for day {:d} part A".format(DAY))
    data = format_input(input)
    computer = ComputeSystem(data)
    computer.run()
    x = computer.getx()
    sig_strength = []
    for i in range(19,len(x), 40):
        print(i+1,x[i])
        sig_strength.append((i+1)*x[i])
    answear = sum(sig_strength)
    print("Result:", answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:d} part B".format(DAY))
    answear = None
    if expected:
        assert answear==expected

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    partA(item_list, expected=14040)
    partB(item_list)

