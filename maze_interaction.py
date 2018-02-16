from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import readchar
import os
import random

# def spawnLocation(board,noRow,noCol):
#     row = 1
#     col = 23
#     if board.state[row][col] != '#':
#         return row,col

keyboard = Controller()
br = Board()
br.initialise()
pRow, pCol = 2, 23
# pRow, pCol = random.randint(1, br.h),random.randint(1, br.w)
p = Player(br, pRow, pCol)
br.playerPosR, br.playerPosC = p.currR, p.currC

os.system('cls' if os.name == 'nt' else 'clear')

br.display()
print p.currR, ",", p.currC
print "Score:", p.score

x = True
while x == True:
    c = readchar.readchar()
    if c == 'w':
        p.moveUp()
        print p.currR,p.currC
        p.winConditionCheck()
    elif c == 's':
        p.moveDown()
        print p.currR,p.currC
        p.winConditionCheck()
    elif c == 'a':
        p.moveLeft()
        print p.currR,p.currC
        p.winConditionCheck()
    elif c == 'd':
        p.moveRight()
        print p.currR,p.currC
        p.winConditionCheck()
    elif c == 'q':
        print "Quitting.."
        x = False
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    br.playerPosR = p.currR
    br.playerPosC = p.currC
    br.display()

    print p.currR, ",", p.currC
    print "Score:", p.score
