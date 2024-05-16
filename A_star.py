import math
from Puzzle import Puzzle
import time as t
import sys
import queue
import json

def Manhattan(puzzle):
    distance = 0
    for i in range(puzzle.height):
        for j in range(puzzle.width):
            if puzzle.grid[i][j]!=0:
                if puzzle.grid[i][j] != i * puzzle.width + j + 1:
                    targetx = math.floor((puzzle.grid[i][j] - 1)/puzzle.width)
                    targety = (puzzle.grid[i][j] - 1)%puzzle.width
                    distance += math.fabs(targetx - i)
                    distance += math.fabs(targety - j)
    return distance

def Hamming(puzzle):
    distance = 0
    for i in range(puzzle.height):
        for j in range(puzzle.width):
            if i == puzzle.height - 1 and j == puzzle.width - 1:
                if puzzle.grid[i][j] != 0:
                    distance += 1
            else:
                if puzzle.grid[i][j] != i * puzzle.width + j + 1:
                    distance += 1
    return distance

class State():
    def __init__(self, puzzle, moves, depth, metrics):
        self.puzzle = puzzle
        self.moves = moves
        self.G = depth
        if moves:
            puzzle.move(moves[-1])
        if metrics == "hamm":
            self.H = Hamming(self.puzzle)
        else:
            self.H = Manhattan(self.puzzle)

    def __eq__(self, other):
        return self.get_distance() == other.get_distance()

    def __lt__(self, other):
        return self.get_distance() < other.get_distance()

    def reverse_direction(self):
        if self.moves == '':
            return 'X'
        if self.moves[-1] == 'L':
            return 'R'
        if self.moves[-1] == 'R':
            return 'L'
        if self.moves[-1] == 'U':
            return 'D'
        if self.moves[-1] == 'D':
            return 'U'

    def get_distance(self):
        return self.H + self.G


class A_star:
    def __init__(self, puzzle, metrics):
        self.puzzle = puzzle
        self.metrics = metrics
        self.states = queue.PriorityQueue()
        self.depth = 0
        self.visited = 0
        self.processed = 0

    def solve(self):
        self.start = t.time()

        first_state = State(self.puzzle, '', 0, self.metrics)
        self.states.put(first_state)
        self.visited += 1

        tmp = -2
        while ( tmp == -2 ):
            tmp = self.check_state(self.states.get())

        duration = (t.time() - self.start)
        duration *= 1000
        return tmp, self.depth, self.visited, self.processed, duration


    def check_state(self, state):
        if (t.time() - self.start > 20):
            return -1
        self.processed += 1
        if (state.puzzle.check_if_correct()):
            return state.moves
        else:
            for key in ['L','R','U','D']:
                if key != state.reverse_direction():
                    puzzle = Puzzle(self.puzzle.width, self.puzzle.height, json.loads(json.dumps(state.puzzle.grid)))
                    newState = State(puzzle, state.moves+key, state.G + 1, self.metrics)
                    self.visited += 1
                    if len(newState.moves) > self.depth:
                        self.depth = len(newState.moves)
                    self.states.put(newState)
            return -2

#puzzlemap = [[1,2,4,0],[5,6,3,8],[9,11,7,12],[13,10,14,15]]
#puzzle = Puzzle(4,4, puzzlemap)
#astar = A_star(puzzle, "hamm")
#wynik, gl_rek, stany_odw, stany_przet, czas = astar.solve()
#print(wynik)