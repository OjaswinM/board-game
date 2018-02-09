from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import readchar

keyboard = Controller()
br = Board()
br.initialise()
p = Player(br)

#p.moveRight()
#br.playerPosR = p.currY
#br.playerPosC = p.currX
#br.display()

c = readchar.readchar()
print c
