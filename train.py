from board import Board
from player import Player
import numpy as np
import random

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

def training(board,player,R,Q):
    row,col = spawnLocation(board.w,board.h)
    player.curC = col
    player.currR = row
