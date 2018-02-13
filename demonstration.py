from board import Board
from player import Player
from pynput.keyboard import Key, Controller
import os
import numpy as np

loadedArray = np.load('trained_set.npz')

def display(numpyArray):
    for i in range(1, br.h + 1):
        for j in range(1, br.w + 1):
            print Q[i, j],
        print '\n'

Q = loadedArray['Q']
# print Q
display(Q)
