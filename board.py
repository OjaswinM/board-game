height = 10
width = 10
cheeseR = 8
cheeseC = 9
class Board:
    def __init__(self,h=height,w=width, row = 1, col = 1):
        self.h = h
        self.w = w
        self.state = []
        self.playerPosR = row
        self.playerPosC = col
        self.goalC = cheeseC
        self.goalR = cheeseR

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
        for i in range(1,8):
            self.state[2][i] = '#'
        self.state[self.playerPosC][self.playerPosR] = 'P'



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
        for i in range(1,8):
            self.state[2][i] = '#'

        self.updatePos()

    def display(self):
        self.reset()
        for row in self.state:
            print ' '.join(row)
