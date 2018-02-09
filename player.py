from board import *

class Player(Board):
    def __init__(self, brd, x = 1, y = 1):
        self.currX = x
        self.currY= y
        self.moves = []
        self.board = brd.state

    def moveLeft(self):
        if self.board[self.currX - 1][self.currY] != '#':
            self.currX -= 1
            self.moves.append((self.currX, self.currY))
    def moveRight(self):
        if self.board[self.currX + 1][self.currY] != '#':
            self.currX += 1
            self.moves.append((self.currX, self.currY))
    def moveUp(self):
        if self.board[self.currX][self.currY - 1] != '#':
            self.currY -= 1
            self.moves.append((self.currX, self.currY))
    def moveDown(self):
        if self.board[self.currX][self.currY + 1] != '#':
            self.currY += 1
            self.moves.append((self.currX, self.currY))
