from board import Board
from player import Player
import numpy as np

def initRewards(R,row,col):
    R[row-1,col-1] = 100

br = Board()
R = np.zeros((br.h,br.w))
initRewards(R,br.goalR,br.goalC)
print R
