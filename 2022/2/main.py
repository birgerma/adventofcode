# importing sys
import sys
 
# adding common to the system path
sys.path.insert(0, '../')
 
from common.io import *

def compute_result(expected, myMove):
  if expected==myMove:
    return 1 #Draw
  elif myMove == 'rock' and expected == 'scissor':
    return 2 # Win, rock beats scissors
  elif myMove == 'paper' and expected == 'rock':
    return 2 # Win, paper beats rock
  elif myMove == 'scissor' and expected == 'paper':
    return 2 # Win, scissors beats paper
  else:
    return 0 # Lost
def compute_points(expected, myMove):
  if myMove == 'rock':
    p=1
  elif myMove == 'paper':
    p=2
  elif myMove == 'scissor':
    p=3

  p += 3*compute_result(expected, myMove)
  #print(expected, myMove, p)
  return p

def get_move(m):
  if m=='A' or m=='X':
    return 'rock'
  elif m=='B' or m=='Y':
    return 'paper'
  elif m=='C' or m=='Z':
    return 'scissor'
  else:
    print("Error")
    quit()
    
def get_moves(move_str):
  moves = move_str.split(" ")
  expected = get_move(moves[0])
  myMove = get_move(moves[1])
  return expected, myMove

# 5760 too low
# 9809 too low
def partA(move_list):
    points = 0
    for m in move_list:
      expected, myMove = get_moves(m)
      points += compute_points(expected, myMove)
    assert points==11906
    print("Total score:",points)
  

def get_lose_move(move):
  if move=='rock':
    return 'scissor'
  elif move=='paper':
    return 'rock'
  elif move=='scissor':
    return 'paper'

def get_win_move(move):
  if move=='rock':
    return 'paper'
  elif move=='paper':
    return 'scissor'
  elif move=='scissor':
    return 'rock'

def get_counter_move(expected, code):
  if code == 'X': # Should lose
    return get_lose_move(expected)
  elif code == 'Y': # Should make draw
    return expected
  elif code == 'Z': # Should win
    return get_win_move(expected)
  else:
    print("ERROR 2")
    quit()

def partB(move_list):
    print("Solve for problem B day 2")
    points = 0
    for m in move_list:
      expected, _ = get_moves(m)
      myMove = get_counter_move(expected, m.split(" ")[1])
      points += compute_points(expected, myMove) 
    assert points==11186
    print("Points:", points)
if __name__=='__main__':
    print("Solve for problem 1 day 1")
    data = read_file('input.txt')
    move_list = data.split('\n')
    move_list = [i for i in move_list if i]
    partA(move_list)
    partB(move_list)

