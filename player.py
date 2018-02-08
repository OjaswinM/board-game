class Player:
    def __init__(self, board, x = 1, y = 1):
        self.currX = x
        self.currY= y
        self.moves = []

    def moveUp(self):
        if board[self.currX - 1][self.currY] != '#':
            self.currX -= 1
            self.moves.append((self.currX, self.currY))
    def moveDown(self):
        if board[self.currX + 1][self.currY] != '#':
            self.currX += 1
            self.moves.append((self.currX, self.currY))
    def moveLeft(self):
        if board[self.currX][self.currY - 1] != '#':
            self.currY -= 1
            self.moves.append((self.currX, self.currY))
    def moveRight(self):
        if board[self.currX][self.currY + 1] != '#':
            self.currY += 1
            self.moves.append((self.currX, self.currY))

