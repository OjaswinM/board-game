from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import readchar
import os

h = 20
w = 20

cheeseR = 13
cheeseC = 15

keyboard = Controller()
br = Board()
br.initialise()
p = Player(br)

#p.moveRight()
#br.playerPosR = p.currY
#br.playerPosC = p.currX
#br.display()
x = True

br.display()
while x == True:
    c = readchar.readchar()
    if c == 'w':
        p.moveUp()
    elif c == 's':
        p.moveDown()
    elif c == 'a':
        p.moveLeft()
    elif c == 'd':
        p.moveRight()
    elif c == 'q':
        print "Quitting.."
        x = False
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    br.playerPosR = p.currY
    br.playerPosC = p.currX
    br.display()
    print p.fitness
