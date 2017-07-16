# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:42:13 2017

@author: chen2
"""
import numpy as np
x=0
board = np.empty([x,x])
steps = 0
player = {'0':None,'1':None}
number = ''

def print_horiz_line():
    print('-----'*x)
       
def print_vert_line(i):
    for j in range(x):
        print('|{:>3} '.format(str(board[i][j])), end='')
    print('|')
        

def display_board(x):    
        
    for i in range(x):
        print_horiz_line()
        print_vert_line(i)
    print_horiz_line()
    
    
def initial_board():
    global x 
    global board
    x = int(input("How many cells on each side do you want?"))
    print('The size of your gameboard is {}'.format(x**2))
    board =np.arange(1,(x**2)+1,1).reshape(x,x)
    print(board)
    board = board.tolist()
  
    

def player_input():
    global steps
    steps +=1
    choice = int(input('In which cell do you want to place your mark?'))
    if 1<=choice<=x**2:
        if board[(choice-1)//x][(choice-1)%x] == choice:
            board[(choice-1)//x][(choice-1)%x] = setMark()
        else:
            print("This cell is already taken")
    else:
        print("The cell does not exist")

def setMark():
    if steps%2==0:
        return 'O'
    else:
        return 'X'
    
def checkWin():
    for i in range(x):
        if len(set(board[i]))<=1:
            return True
        elif len(set(index[i] for index in board))<=1:
            return True
        else:
            return False

import random  
def chooseFirst():
    global player
    player['0']=input("What is the first player's name?")
    player['1']=input("What is the second player's name?")
    global number
    number = str(random.randint(0,1))
    print('{} goes first'.format(player[number]))

def replay():
    return input('Want to start a new game? y/n')=='y'  



print("Welcome to Tic Tac Toe!")

while replay() == True:
    
    initial_board()
    display_board(x)
    chooseFirst()
    while checkWin()!=True:
        player_input()
        display_board(x)
        if all(isinstance(x, str) for x in board):
            print("It is a tie")
            break
    print('Game Over')
    if steps%2==1:
        print(player[number],"is the winner!")
    else:
        print(player[str(abs(int(number)-1))], "is the winner!")
    
    x=0
    board = np.empty([x,x])
    steps = 0
      