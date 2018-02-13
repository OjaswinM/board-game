from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import os
import numpy as np
import board
import time

loadedArray = np.load('trained_set.npz')

def display(numpyArray):
    for i in range(1, board.height + 1):
        for j in range(1, board.width + 1):
            print Q[i, j],
        print '\n'

Q = loadedArray['Q']
# print Q
display(Q)
