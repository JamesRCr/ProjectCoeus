""" Sudoku Solver """

import numpy as np


def label(func):
    return func

Helper = label
Main = label


class Entry:
    def __init__(self, initial_value):
        self._entry = initial_value
        self.possibilities = []

    @property
    def entry(self):
        return self._entry

    @entry.setter
    def entry(self, value):
        self._entry = value


grid = [[Entry(0) * 9] * 9]


def pprint(grid):
    print(np.matrix(grid))


@Helper
def checker(y, x, n):
    global grid
    # check row
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    # check column
    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    # form 3x3 box coordinates
    x0 = (x//3)*3
    y0 = (y//3)*3
    # check the 3x3 box
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


@Main
def solve():
    pass
    """
    - Iterates through each entry
    - Checks if entry is 0
    - Checks all possible solutions for that entry
    - If only one solution, that entry takes the solution
    - After running through all entries, log the current state and iterate again
    - If current log is the same as previous log, a final state has been reached
    """


if __name__ == '__main__':
    solve()
    pprint(grid)
