

import time as t
import json

class Puzzle:
    width = 4
    height = 4
    x = 0
    y = 0
    grid = []
    def __init__(self, width, height, grid,children=[]):
        self.width = width
        self.height = height
        self.grid = grid
        self.children = children
        for i in range(0,self.width): #szukanie zera
            for j in range(0,self.height):
                if self.grid[i][j] == 0:
                    self.x = i
                    self.y = j


    def posmoves(self, order):
        possible = []
        for i in range(0,len(order)):
            possible.append(order[i])
        nextMoves = []
        tmp = []
        if self.x == 0:
            tmp.append("U")
        if self.x == self.height - 1:
            tmp.append("D")
        if self.y == 0:
            tmp.append("L")
        if self.y == self.width - 1:
            tmp.append("R")
        for x in range(0, len(possible)):
            licznik = 0
            for y in range(0, len(tmp)):
                if possible[x] == tmp[y]:
                    licznik += 1
            if licznik < 1:
                nextMoves.append(possible[x])
        return nextMoves


    def move(self, direction):
        if direction == 'D':
            if self.x == self.height - 1:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x + 1][self.y]
            self.grid[self.x + 1][self.y] = 0
            self.x = self.x + 1
            return 0
        if direction == 'U':
            if self.x == 0:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x - 1][self.y]
            self.grid[self.x - 1][self.y] = 0
            self.x = self.x - 1
            return 0
        if direction == 'L':
            if self.y == 0:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x][self.y - 1]
            self.grid[self.x][self.y - 1] = 0
            self.y = self.y - 1
            return 0
        if direction == 'R':
            if self.y == self.width - 1:
                return -1
            self.grid[self.x][self.y] = self.grid[self.x][self.y + 1]
            self.grid[self.x][self.y + 1] = 0
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
        for i in range(self.width):
            for j in range(self.height):
                if i == self.width - 1 and j == self.height - 1:
                    if self.grid[i][j] != 0:
                        return False
                else:
                    if self.grid[i][j] != i * self.width + j + 1:
                        return False
        return True


    def get_children(self,direction):
        child = Puzzle(4,4,json.loads(json.dumps(self.grid)))
        child.move(direction)
        self.children.append(child.grid)
        return child.grid

    def append_children(self, moves, puzzle1, fulllist, queue):
        for m in moves:
            q = puzzle1.get_children(m)
            queue.append(q)
            fulllist.append([q,m])
        return queue

def czyodwiedzono(puzzle: Puzzle, Been_tab):
    be = puzzle
    if be in Been_tab:
        return True

    Been_tab.append(puzzle)
    return False

def pathall(grid1, pathh, fulllist):
    for i in range(0,len(fulllist)):
        if grid1 == fulllist[i][0]:
            pathh += str(fulllist[i][1])
            puzz = Puzzle(4,4,grid1)
            puzz.reverse_move(fulllist[i][1])
            grid = puzz.grid
            return pathh, grid
    return "-1", grid1

def revstr(str):
    strr = str[::-1]
    return strr

class BFS:
    fulllist = []
    Been_tab = []
    fpath = ""
    def __init__(self, puzzle, order):
        self.puzzle = puzzle
        self.order = order

    def solve(self, queue, pm):
        start = t.time()
        booly = True
        end1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        tmp = Puzzle(4,4,pm).grid
        fpath = ""
        Been_tab = []
        fulllist = []
        print(queue[0])
        while (booly):
            puzzle = Puzzle(4, 4, queue[0])
            if puzzle.check_if_correct():
                print("correct")
                for i in range(0, 25):
                    if end1 == tmp:
                        break
                    else:
                        fpath, grid1 = pathall(end1, fpath, fulllist)
                endtime = (t.time() - start)
                endtime *= 1000
                if fpath == "-1":
                    return endtime, len(Been_tab), len(fulllist), "-1", "0"
                else:
                    return endtime, len(Been_tab), len(fulllist), revstr(fpath), len(fpath)
            if not czyodwiedzono(puzzle, Been_tab):
                available = puzzle.posmoves(self.order)
                puzzle.append_children(available, puzzle, fulllist, queue)
            if (t.time() - start > 20) or (queue[0] == end1):
                booly = False
            queue.pop(0)
        for i in range(0, 25):
            if end1 == tmp:
                break
            else:
                fpath, grid1 = pathall(end1, fpath, fulllist)
        endtime = (t.time() - start)
        endtime *=1000
        return endtime, len(Been_tab), len(fulllist), revstr(fpath), len(fpath)

"""
lines(puzzlemap)
puzzlemap.pop(0)

#kolejnosc kolejnych ruchow
order = sys.argv[2]

puzzle = Puzzle(4,4,puzzlemap)
queue.append(puzzle.grid)
bfs = BFS(puzzle, order)
time, bt, fl, fp, dp = bfs.solve(queue,puzzlemap)


print("path")
print(fp)
print("depth")
print(dp)
print("visited")
print(fl)
print("processed")
print(bt)
print("time")
print(time)
"""