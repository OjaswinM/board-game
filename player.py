from board import Board

cheeseR = 13
cheeseC = 15

class Player(Board):
    def __init__(self, brd, x = 1, y = 1):
        self.currX = x
        self.currY= y
        self.moves = []
        self.board = brd.state
        self.fitness = None

    def fitnessCalc(self):
        self.fitness = ((cheeseR - self.currX) ** 2 + (cheeseC - self.currY) ** 2) ** 0.5

    def moveLeft(self):
        if self.board[self.currX - 1][self.currY] != '#':
            self.currX -= 1
            self.moves.append((self.currX, self.currY))
            self.fitnessCalc()
    def moveRight(self):
        if self.board[self.currX + 1][self.currY] != '#':
            self.currX += 1
            self.moves.append((self.currX, self.currY))
            self.fitnessCalc()
    def moveUp(self):
        if self.board[self.currX][self.currY - 1] != '#':
            self.currY -= 1
            self.moves.append((self.currX, self.currY))
            self.fitnessCalc()
    def moveDown(self):
        if self.board[self.currX][self.currY + 1] != '#':
            self.currY += 1
            self.moves.append((self.currX, self.currY))
            self.fitnessCalc()
