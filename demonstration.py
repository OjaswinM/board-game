from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import os
import numpy as np
import board
import time
import random
loadedArray = np.load('trained_set.npz')

Q = loadedArray['Q']

def findMaxPosition(Q,row,col):
    maximum = max(Q[row+1,col],Q[row-1,col],Q[row,col-1],Q[row,col+1])
    if Q[row+1, col] == maximum:
        return 1  #MoveDown
    elif Q[row-1, col] == maximum:
        return 2   #MoveUp
    elif Q[row, col-1] == maximum:
        return 3   #MoveLeft
    else:
        return 4   #MoveRight

br = Board()
pRow, pCol = random.randint(1, br.h),random.randint(1, br.w)
p = Player(br, pRow, pCol)
br.playerPosR, br.playerPosC = p.currR, p.currC
br.initialise()
br.reset()

os.system('cls' if os.name == 'nt' else 'clear')

br.display()
print p.currR, ",", p.currC
print "Fitness: ", p.fitness
print "Score: ", p.score

x = True
while x == True:
    direction = findMaxPosition(Q, p.currR, p.currC)
    if direction == 1:
        p.moveDown()
    elif direction == 2:
        p.moveUp()
    elif direction == 3:
        p.moveLeft()
    elif direction == 4:
        p.moveRight()
    p.winConditionCheck()
    br.playerPosR = p.currR
    br.playerPosC = p.currC
    os.system('cls' if os.name == 'nt' else 'clear')
    br.display()
    print p.currR, ",", p.currC
    print "Fitness: ", p.fitness
    print "Score: ", p.score

    time.sleep(0.1)
