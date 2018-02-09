from board import *
from player import *

br = Board()
br.initialise()

p = Player(br)

p.moveDown()
p.moveRight()
p.moveDown()
p.moveLeft()
p.moveUp()

br.playerPosC = p.currX
br.playerPosR = p.currY

br.display()
