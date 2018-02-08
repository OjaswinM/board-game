height = 5
width = 5

class Board:
    def __init__(self,h=height,w=width):
        self.h = h
        self.w = w
        self.state = []

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

    def display(self):
        for row in self.state:
            print ' '.join(row)
