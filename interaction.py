from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import readchar
import os

keyboard = Controller()
br = Board()
br.initialise()
p = Player(br)
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