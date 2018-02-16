from board import Board
from player import Player
import numpy as np
import random
import time
import os
import matplotlib.pyplot as plt
import time, threading, thread

def watchdog_timer(state):
    time.sleep(0.5)
    if not state['completed']:
        thread.interrupt_main()

gammaFactor = 0.85
try:
    os.remove('trained_set.npz')
except OSError:
    pass

# def display(numpyArray):
#     for i in range(1, br.h + 1):
#         for j in range(1, br.w + 1):
#             print Q[i,j],
#         print '\n'

def initRewards(board,R,row,col):
    R[row,col] = 1000
    for i in range(1,board.h +1):
        for j in range(1,board.w+1):
            if board.state[i][j] == '#':
                R[i][j] = -1

def encloseMinusOne(R):
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if i == 0 or i == R.shape[0] - 1:
                R[i, j] = -1
            if j == 0 or j == R.shape[1] - 1:
                R[i, j] = -1

def getQ(R,Q,row,col):
    return (R[row,col] + gammaFactor*(findMax(Q,row,col)))

def findMax(Q,row,col):
    return max(Q[row+1,col],Q[row-1,col],Q[row,col-1],Q[row,col+1])

def spawnLocation(board,noRow,noCol):
    row = random.randint(1,noRow)
    col = random.randint(1,noCol)
    if board.state[row][col] != '#':
        return row,col
    else:
        return spawnLocation(board,noRow,noCol)

def training(R,Q,board,player):
    while True:
        state = {'completed': False}
        watchdog = threading.Thread(target=watchdog_timer, args=(state,))
        watchdog.daemon = True
        watchdog.start()
        try:
            row,col = spawnLocation(board,board.w,board.h)
            player.currC = col
            player.currR = row
            board.playerPosC = player.currC
            board.playerPosR = player.currR
            board.display()

            while((player.currR != board.goalR) or (player.currC != board.goalC)):
                moveOneStep(player)
                Q[player.currR,player.currC] = getQ(R,Q,player.currR,player.currC)
            state['completed'] = True
        except KeyboardInterrupt:
            # this would be the place to log the timeout event
            pass
        else:
            break

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
br.display()
R = np.zeros((br.h + 2,br.w + 2))
encloseMinusOne(R)
initRewards(br,R,br.goalR,br.goalC)
Q = np.zeros((br.h + 2,br.w + 2),dtype=float)
encloseMinusOne(Q)
#print R, Q
for i in range(1000):
   training(R,Q,br,p)
   print i



np.set_printoptions(threshold=np.nan)
np.savez_compressed('trained_set.npz', Q = Q)
plt.imshow(Q)
plt.show()

display(Q)
