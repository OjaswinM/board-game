import numpy as np
loadedArray = np.load('Maze1.npz')
maze = loadedArray['R']
height = 50
width = 50
cheeseR = 3
cheeseC = 3
class Board:
    def __init__(self,h=height,w=width, row = 1, col = 1):
        self.h = h
        self.w = w
        self.state = []
        self.playerPosR = row
        self.playerPosC = col
        self.goalC = cheeseC
        self.goalR = cheeseR

    # def initMaze(self):
        # for i in range(1,11):
        #     if i != 8:
        #         self.state[2][i] = '#'
        # for i in range(4,11):
        #     self.state[4][i] = '#'
        # for i in range(1,3):
        #     self.state[4][i] = '#'
        # for i in range(1,10):
        #     if i !=7:
        #         self.state[6][i] = '#'
        # for i in range(8,11):
        #     self.state[7][i] = '#'
        # for i in range(2,9):
        #     self.state[8][i] = '#'


    def updatePos(self):
        self.state[self.playerPosR][self.playerPosC] = 'P'
        self.state[self.goalR][self.goalC] = 'O'

    def initialise(self):
        for i in range(self.h+2):
            self.state.append(['_']*(self.w+2))
        for i in range(self.h+2):
            for j in range(self.w+2):
                if i == 0 or i == (self.h+1):
                    self.state[i][j] = '#'
                    continue
                if j == 0 or j == (self.w+1):
                    self.state[i][j] = '#'
                    continue
        self.state[self.playerPosC][self.playerPosR] = 'P'
        # self.initMaze()

    def reset(self):
        for i in range(self.h+2):
            for j in range(self.w+2):
                if i == 0 or i == (self.h+1):
                    self.state[i][j] = '#'
                    continue
                if j == 0 or j == (self.w+1):
                    self.state[i][j] = '#'
                    continue
                self.state[i][j] = '_'
        # self.initMaze()
        self.updatePos()

    def display(self):
        self.reset()
        for row in self.state:
            print ' '.join(row)
