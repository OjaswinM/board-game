from board import Board


class Player(Board):
    def __init__(self, brd, row = 1, col = 1):
        self.currC = col
        self.currR= row
        self.moves = []
        self.board = brd.state
        self.fitness = None
        self.goalC = brd.goalC
        self.goalR = brd.goalR

    def fitnessCalc(self):
        self.fitness = ((self.goalR - self.currR) ** 2 + (self.goalC - self.currC) ** 2) ** 0.5

    def moveLeft(self):
        if self.board[self.currC - 1][self.currR] != '#':
            self.currC -= 1
            self.moves.append((self.currC, self.currR))
            self.fitnessCalc()
    def moveRight(self):
        if self.board[self.currC + 1][self.currR] != '#':
            self.currC += 1
            self.moves.append((self.currC, self.currR))
            self.fitnessCalc()
    def moveUp(self):
        if self.board[self.currC][self.currR - 1] != '#':
            self.currR -= 1
            self.moves.append((self.currC, self.currR))
            self.fitnessCalc()
    def moveDown(self):
        if self.board[self.currC][self.currR + 1] != '#':
            self.currR += 1
            self.moves.append((self.currC, self.currR))
            self.fitnessCalc()
