import math
import random

class Board:
    map = {-2: "flag", -1: "mine", 0: "empty"}
    grid = []

    def __init__(self, x, y, mines):
        self.x = x
        self.y = y
        self.mines = mines
        self.init_grid(mines)
        self.print_grid()

    def increment_neighbors(self,x,y):
        row_start = max(y - 1, 0)
        row_end = min(y + 1, self.y - 1)
        col_start = max(x - 1, 0)
        col_end = min(x + 1, self.x - 1)
        for row in range(row_start, row_end + 1):
            for col in range(col_start, col_end + 1):
                if self.grid[row][col] != -1:
                    self.grid[row][col] = self.grid[row][col] + 1


    def init_grid(self, mines):
        # initialize the grid
        self.grid = [[0 for j in range(self.x)] for i in range(self.y)]

        # setting up the initial mine pos
        for i in range(mines):
            col = random.randrange(0,self.x)
            row = random.randrange(0,self.y)
            if self.grid[row][col] == -1:
                i = i - 1
            else:
                self.grid[row][col] = -1
                # handling values around mines
                self.increment_neighbors(col,row)
        #self.grid[0][0] = -1
        #self.increment_neighbors(0,0)

        


    def print_grid(self):
        for row in range(self.x):
            print(self.grid[row])

if __name__ == "__main__":
    board1 = Board(8,8,10)

    print(board1.x)
    print(board1.y)
    print(board1.map)    