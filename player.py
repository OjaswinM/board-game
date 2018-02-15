from board import Board
import random

def resetLocation(state,noRow,noCol):
    row = random.randint(1,noRow)
    col = random.randint(1,noCol)
    if state[row][col] != '#':
        return row,col
    else:
        return resetLocation(state,noRow,noCol)

class Player(Board):
    def __init__(self, brd, row = 1, col = 1):
        self.currC = col
        self.currR= row
        self.board = brd.state
        self.goalC = brd.goalC
        self.goalR = brd.goalR
        self.score = 0
        self.sizeR = brd.h
        self.sizeC = brd.w

    def fitnessCalc(self):
        self.fitness = ((self.goalR - self.currR) ** 2 + (self.goalC - self.currC) ** 2) ** 0.5

    def moveLeft(self):
        if self.board[self.currR][self.currC - 1] != '#':
            self.currC -= 1
    def moveRight(self):
        if self.board[self.currR][self.currC + 1] != '#':
            self.currC += 1
    def moveUp(self):
        if self.board[self.currR - 1][self.currC] != '#':
            self.currR -= 1
    def moveDown(self):
        if self.board[self.currR + 1][self.currC] != '#':
            self.currR += 1

    def win(self):
        pRow, pCol = resetLocation(self.board,self.sizeR,self.sizeC)
        self.currR = pRow;
        self.currC = pCol;
        self.score += 1

    def winConditionCheck(self):
        if self.goalR == self.currR and self.goalC == self.currC:
            self.win()
