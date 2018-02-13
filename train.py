from board import Board
from player import Player
import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
gammaFactor = 0.8

def initRewards(R,row,col):
    R[row,col] = 100        #set reward cell as 100 in R        #sets reward as 100

def encloseMinusOne(R):
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if i == 0 or i == R.shape[0] - 1:
                R[i, j] = -1
            if j == 0 or j == R.shape[1] - 1:
                R[i, j] = -1        #enclose numpy array with -1           #encloses numpy with -1

def getQ(R,Q,row,col):          #get the new value of Q
    return (R[row,col] + gammaFactor*(findMax(Q,row,col)))

def findMax(Q,row,col):
    return max(Q[row+1,col],Q[row-1,col],Q[row,col-1],Q[row,col+1])

def spawnLocation(noRow,noCol):
    location = []
    row = random.randint(1,noRow)
    col = random.randint(1,noCol)
    return row,col

def training(R,Q,board,player):
    row,col = spawnLocation(board.w,board.h)
    player.currC = col
    player.currR = row
    board.playerPosC = player.currC
    board.playerPosR = player.currR
    board.display()
    i=1
    while((player.currR != board.goalR) or (player.currC != board.goalC)):
        moveOneStep(player)
        Q[player.currR,player.currC] = getQ(R,Q,player.currR,player.currC)
        i = i+1
        # board.playerPosC = player.currC
        # board.playerPosR = player.currR
        # board.display()
        # print player.currR, player.currC
        # print board.goalR, board.goalC

    # os.system('cls' if os.name == 'nt' else 'clear')
    # time.sleep(0.4)

def moveOneStep(player):
    temp = random.randint(1,4)
    if temp == 1:
        player.moveUp()
    elif temp == 2:
        player.moveDown()
    elif temp == 3:
        player.moveLeft()
    else:
        player.moveRight()

br = Board()
br.initialise()
p = Player(br)

R = np.zeros((br.h + 2,br.w + 2))
encloseMinusOne(R)
initRewards(R,br.goalR,br.goalC)
Q = np.zeros((br.h + 2,br.w + 2),dtype=int)
encloseMinusOne(Q)
for i in range(1000):
    training(R,Q,br,p)
    print i
np.set_printoptions(threshold=np.nan)
# def display(npBoard):
#     displayBoard = npBoard
#     for emt in displayBoard:
#         emt = str(emt)
#         print(emt)
#         # for row in displayBoard:
#         #     print ' '.join(row)

plt.imshow(Q)
plt.show()
# def normalise(numpyArray):
#     numpyArray = (numpyArray - np.amax(numpyArray))/(np.amax(numpyArray) - np.amin(numpyArray))
# normalise(Q)
print Q
