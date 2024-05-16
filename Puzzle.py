class Puzzle:
    width = 4
    height = 4
    x = 0
    y = 0
    grid = []
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == 0:
                    self.x = i
                    self.y = j

    def move(self, direction):
        if direction == 'U':
            if self.x == self.height-1:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x+1][self.y]
            self.grid[self.x+1][self.y] = 0
            self.x = self.x + 1
            return 0
        if direction == 'D':
            if self.x == 0:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x-1][self.y]
            self.grid[self.x-1][self.y] = 0
            self.x = self.x - 1
            return 0
        if direction == 'R':
            if self.y == 0:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x][self.y-1]
            self.grid[self.x][self.y-1] = 0
            self.y = self.y - 1
            return 0
        if direction == 'L':
            if self.y == self.width-1:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x][self.y+1]
            self.grid[self.x][self.y+1] = 0
            self.y = self.y + 1
            return 0
        
    def reverse_move(self, direction):
        if direction == 'L':
            return self.move('R')
        if direction == 'R':
            return self.move('L')
        if direction == 'U':
            return self.move('D')
        if direction == 'D':
            return self.move('U')

    def check_if_correct(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == self.height - 1 and j == self.width - 1:
                    if self.grid[i][j] != 0:
                        return False
                else:
                    if self.grid[i][j] != i * self.width + j + 1:
                        return False
        return True




    
