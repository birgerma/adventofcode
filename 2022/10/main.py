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
        self.sprite = 1

    def run(self):
        for ins in self.instructions:
            x = self.x[-1]
            if ins[0]=='addx':
                self.x.append(x) # Clock cycle 1
                x+=ins[1]
                self.x.append(x)
            elif ins[0]=='noop':
                self.x.append(x)
    def getx(self):
        return self.x

    def _in_sprite(self, x):
        pos = x%40
        print("Mod x pos:", pos)
        if pos<self.sprite-1 or pos>self.sprite+1:
            return False
        return True

    def draw(self):
        screen = []
        for i in range(len(self.x)):
            x=self.x[i]
            self.sprite = x
            if self._in_sprite(i):
                print("Cycle:", i, "sprite pos:",self.sprite, "x=", x," draw #")
                screen.append('#')
            else:
                print("Cycle:", i, "sprite pos:",self.sprite,  "x=", x," draw .")
                screen.append('.')
            print(screen)
            print("Sprite pos:", self.sprite)
            #if i>2:
            #    quit()
        self.screen = screen

    def show_screen(self):
        WIDTH = 40
        for i in range(len(self.screen)):
            print(self.screen[i], end='')
            if i>0 and (i+1)%WIDTH==0:
                print()



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
    data = format_input(input)
    computer = ComputeSystem(data)
    computer.run()
    computer.draw()
    answear = None
    print("Print screen")
    computer.show_screen()
    print("Should print:", "ZGCJZJFL")

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    #partA(item_list, expected=14040)
    partB(item_list, expected="ZGCJZJFL")

