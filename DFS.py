from Puzzle import Puzzle
import time as t

class State:
    direction = 'L'
    reverse_direction = 'R'
    children = {'L':None, 'R':None, 'U':None, 'D':None}
    def __init__(self, direction):
        self.direction = direction
        if self.direction == 'L':
            self.reverse_direction = 'R'
        elif self.direction == 'R':
            self.reverse_direction = 'L'
        elif self.direction == 'U':
            self.reverse_direction = 'D'
        elif self.direction == 'D':
            self.reverse_direction = 'U'
        self.children = {'L':None, 'R':None, 'U':None, 'D':None}

class DFS:
    max_depth = 20
    current_depth = 0 
    depth = 0
    visited = 0
    processed = 0
    moves = ""
    def __init__(self, puzzle, order):
        self.puzzle = puzzle
        self.order = order
    
    def solve(self):
        self.start = t.time()
        self.visited += 4
        for i in range(4):
            self.depth = 0
            self.current_depth = 0
            state = State(self.order[i])
            result = self.checkState(state)
            if (result == -2 or result != -1):
                break
        duration = (t.time() - self.start)
        duration *= 1000
        if result == -2:
            result = -1
        return result, self.depth, self.visited, self.processed, duration

    def checkState(self, state):
        if (t.time() - self.start > 20):
            return -2
        self.processed += 1
        self.current_depth +=1
        if (self.current_depth > self.depth):
            self.depth = self.current_depth
        if (self.puzzle.move(state.direction) == -1):
            return -1
        if self.puzzle.check_if_correct() == True:
            return state.direction;
        if (self.current_depth >= self.max_depth):
            self.puzzle.reverse_move(state.direction)
            return -1
        for key in state.children:
            if key != state.reverse_direction:
                state.children[key] = State(key)
                self.visited += 1
        for i in range(4):
            if (state.children[self.order[i]] is not None):
                tmp = self.checkState(state.children[self.order[i]])
                self.current_depth -= 1
                if tmp == -2:
                    return -2
                if tmp != -1:
                    return state.direction + tmp 
        self.puzzle.reverse_move(state.direction)
        return -1

