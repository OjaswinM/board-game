from board import Board
from player import Player
import numpy as np

def initRewards(R,row,col):
    R[row,col] = 100

br = Board()
R = np.zeros((br.h + 2,br.w + 2))

def encloseMinusOne(R):
    for i in range(R.shape[0]):
        for j in range(R.shape[1]):
            if i == 0 or i == R.shape[0] - 1:
                R[i, j] = -1
            if j == 0 or j == R.shape[1] - 1:
                R[i, j] = -1
