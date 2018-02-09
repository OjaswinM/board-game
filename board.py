height = 20
width = 20

class Board:
    def __init__(self,h=height,w=width):
        self.h = h
        self.w = w
        self.state = []
        self.playerPosR = 1
        self.playerPosC = 1
        self.goalR = h-5
        self.goalC = w-7

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
        self.state[self.playerPosR][self.playerPosC] = 'P'



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
        self.updatePos()

    def display(self):
        self.reset()
        for row in self.state:
            print ' '.join(row)
