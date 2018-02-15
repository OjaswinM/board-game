from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import readchar
import os
import random
keyboard = Controller()
br = Board()
# br.initialise()
pRow, pCol = random.randint(1, br.h),random.randint(1, br.w)
p = Player(br, pRow, pCol)
br.playerPosR, br.playerPosC = p.currR, p.currC
br.initialise()
br.reset()

os.system('cls' if os.name == 'nt' else 'clear')

br.display()
print p.currR, ",", p.currC
print "Fitness:", p.fitness
print "Score:", p.score

x = True
while x == True:
    c = readchar.readchar()
    if c == 'w':
        p.moveUp()
        p.winConditionCheck()
    elif c == 's':
        p.moveDown()
        p.winConditionCheck()
    elif c == 'a':
        p.moveLeft()
        p.winConditionCheck()
    elif c == 'd':
        p.moveRight()
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
    print "Fitness:", p.fitness
    print "Score:", p.score
