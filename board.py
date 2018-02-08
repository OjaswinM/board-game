height = 5
width = 5

class Board:
    def __init__(self,h=height,w=width):
        self.h = h
        self.w = w
        self.state = []
        self.playerPosR = 1
        self.playerPosC = 1

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
                if i == self.playerPosR and j == self.playerPosC:
                    self.state[i][j] = 'P'


    def display(self):
        for row in self.state:
            print ' '.join(row)

br = Board()
br.initialise()
br.display()
