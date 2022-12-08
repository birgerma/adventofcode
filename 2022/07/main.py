# importing sys
import sys
import os
 
from treelib import Tree, Node

# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

DAY = int(os.getcwd().split('/')[-1])

def parse_line(line):
    line = line.split(" ")
    if line[0]=='$':
        cmd = line[1]
        args = line[2:]
        return {'type':'cmd', 'cmd':cmd, 'args': args}
    elif line[0]=='dir':
        return {'type':'dir', 'name':line[1], 'size':None}
    else:
        # Assume file
        return {'type':'file', 'size':int(line[0]), 'name':line[1]}

def get_child_nodes(tree, node):
    child_ids = node.fpointer
    children = []
    for child_id in child_ids:
        print(child_id)
        children.append(tree.get_node(child_id))
    return children

def cd(dir_tree, current, args):
    if len(args)==1:
        arg = args[0]
        if arg=='.':
            # Do nothing
            return current
        elif arg=='..':
            # Move up one dir
            parent_id = current.bpointer
            current = dir_tree.get_node(parent_id)
            #parent = dir_tree.parent(current)
            #current = parent.identifier
            #current = parent
        else:
            # Move to dir
            print("Current node:", current)
            if current:
                print("Fpointer:",current.fpointer)
                for child in get_child_nodes(dir_tree, current):
                    print("Child:", child)
                    if child.tag==arg:
                        current=child
                        break
            else:
                current = dir_tree.get_node(dir_tree.root)
            #current = arg
    else:
        print("Error, cd can only take one arg, quits")
        quit()
    return current

def get_file_list(input, index):
    flist = []
    while index<len(input):
        output = parse_line(input[index])
        if output['type']=='cmd':
            break
        else:
            flist.append(output)
        index+=1
    return flist

def parse_input(input):
    current = None
    dir_tree = Tree()
    dir_tree.create_node('/','/') # Root node
    i=0
    while i<len(input):
        line = input[i]
        output = parse_line(line)
        print(i,":", output)
        if output['type']=='cmd':
            # Execute command
            if output['cmd']=='cd':
                # Change dir
                current = cd(dir_tree, current, output['args'])
                i+=1
            elif output['cmd']=='ls':
                # Add nodes to tree
                flist = get_file_list(input, i+1)
                for f in flist:
                    name = f['name']
                    size = f['size']
                    dir_tree.create_node(tag=name, parent=current, data=size)
                i+=(len(flist)+1)
        else:
            print("ERROR")
            quit()
    return dir_tree

def compute_size(ftree, node=None):
    if not node:
        node=ftree.get_node(ftree.root)

    #ftree.show()
    #root = ftree.root
    #root_node = ftree.get_node(root)
    if node.data:
        return node.data
    else:
        children = ftree.children(node.identifier)
        total_size = 0
        for child in children:
            size = compute_size(ftree, child)
            total_size+=size
        node.data=total_size
        return node.data

def partA(input, expected=None):
    print("Solve for day {:d} part A".format(DAY))
    file_tree = parse_input(input)
    compute_size(file_tree)
    answear = 0
    for node in file_tree.all_nodes():
        #print(node)
        if node.is_leaf():
            pass
        elif node.data<=100000:
            print(node.identifier,":", node.data)
            answear+=node.data
    if expected:
        assert answear==expected
    print("Result:", answear)

#42476859 Too high
def partB(input, expected=None):
    print("Solve for day {:d} part B".format(DAY))
    file_tree = parse_input(input)
    compute_size(file_tree)
    total_space = 70000000
    needed_space = 30000000
    used_space = file_tree.get_node(file_tree.root).data
    free_space = total_space-used_space
    print("Used space:", used_space)
    print("Free space:", free_space)
    to_remove = needed_space-free_space
    print("Need to remove:", to_remove)
    dir_sizes = []
    answear = 0
    
    for node in file_tree.all_nodes():
        #print(node)
        if node.is_leaf():
            pass
        else:
            dir_sizes.append(node.data)
        #elif node.data>=24933642:
    dir_sizes = sorted(dir_sizes)
    print(dir_sizes)
    # 24 933 642
    dir_sizes = list(filter(lambda x: x>=to_remove, dir_sizes))
    print(dir_sizes)
    answear = dir_sizes[0]
    print("Result:", answear)
    if expected:
        assert answear==expected

if __name__=='__main__':
    data_file = 'input.txt'
    #data_file = 'test.txt'
    item_list = read_list_data(data_file)
    partA(item_list, expected=1517599)
    partB(item_list, expected=2481982)

