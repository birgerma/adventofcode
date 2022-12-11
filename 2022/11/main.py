# importing sys
import sys
import os
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])
class Monkey:

    INDEX = 0
    def __init__(self, items, operation, test, action):
        self.items = items
        self.operation = operation
        self.test = test
        self.action = action
        self.is_included = 0
        self.my_index = Monkey.INDEX
        self.custom_decrease_factor=0
        Monkey.INDEX+=1

    def get_business(self):
        return self.is_included

    def pop_item(self):
        item = self.items[0]
        if len(self.items)>1:
            self.items = self.items[1:]
        else:
            self.items = []
        return item

    def has_items(self):
        return len(self.items)>0


    def do_operation(self, item):
        op = self.operation.copy()
        if op[0]=='old':
            op[0]=item
        if op[2]=='old':
            op[2]=item

        if op[1]=='*':
            res = op[0]*op[2]
        elif op[1]=='+':
            res = op[0]+op[2]
        else:
            print("Error operator")
            quit()
        return res

    def throw_item(self, item, monkeys):
        if item%self.test==0:
            next = self.action[0]
        else:
            next = self.action[1]
        monkeys[next].receive(item)

    def receive(self, item):
        self.items.append(item)

    def do_round(self, monkeys, worry_decrease=True):
        while self.has_items():
            self.is_included+=1
            item = self.pop_item()
            new = self.do_operation(item)
            if worry_decrease:
                new//=3
            else:
                if self.custom_decrease_factor==0:
                    self.custom_decrease_factor=1
                    for m in monkeys:
                        self.custom_decrease_factor*=m.test
                new=new%self.custom_decrease_factor
            self.throw_item(new, monkeys)

    def __str__(self):
        string = ""
        string+="Items:" + ",".join(str(x) for x in self.items)
        string+="\nOperation:" + ",".join(str(x) for x in self.operation)
        string+="\nTest if div by:" + str(self.test)
        string+="\nIf True throw to monkey "+str(self.action[0])
        string+="\nElse throw to monkey "+str(self.action[1])
        return string

def format_input(input):
    monkeys = []
    for i in range(0,len(input), 6):
        items = input[i+1].split(": ")[1]
        items = [int(i) for i in items.split(",")]
        operation = input[i+2].split("= ")[1].strip().split(" ")
        if operation[0]!='old':
            operation[0]= int(operation[0])
        if operation[2]!='old':
            operation[2]=int(operation[2])

        div = int(input[i+3].split(" ")[-1])

        action = []
        a1 = int(input[i+4].split(" ")[-1])
        a2 = int(input[i+5].split(" ")[-1])
        action = [a1, a2]
        monkeys.append(Monkey(items, operation, div, action))
    return monkeys

def partA(input, expected=None):
    print("Solve for day {:d} part A".format(DAY))
    monkeys = format_input(input)
    n_rounds = 20
    for round in range(n_rounds):
        for monkey in monkeys:
            monkey.do_round(monkeys)

    monkey_business = [m.get_business() for m in monkeys]
    monkey_business.sort(reverse=True)
    answear = monkey_business[0]*monkey_business[1]
    print("Answear:", answear)
    if expected:
        assert answear==expected

def partB(input, expected=None):
    print("Solve for day {:d} part B".format(DAY))
    monkeys = format_input(input)
    n_rounds = 10000
    for round in range(n_rounds):
        #print("Round:", round)
        for monkey in monkeys:
            monkey.do_round(monkeys,worry_decrease=False)
    monkey_business = [m.get_business() for m in monkeys]
    monkey_business.sort(reverse=True)
    answear = monkey_business[0]*monkey_business[1]
    print("Answear:", answear)
    if expected:
        assert answear==expected

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    partA(item_list, expected=99852)
    partB(item_list, expected=25935263541)

