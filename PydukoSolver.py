  """ Sudoku Solver """

import numpy as np


def label(func):
    return func

Helper = label
Main = label


grid = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]


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


if __name__ == '__main__':
    solve()
    pprint(grid)
