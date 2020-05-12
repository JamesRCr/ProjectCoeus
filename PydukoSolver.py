""" Sudoku Solver """


def label(func):
    return func


Helper = label
Main = label
Test = label


class Entry:
    def __init__(self, initial_value):
        self._entry = initial_value
        self._possibilities = []

    @property
    def entry(self):
        return self._entry

    @entry.setter
    def entry(self, value):
        self._entry = value

    @property
    def possibilities(self):
        return self._possibilities

    @possibilities.setter
    def possibilities(self, value):
        self._possibilities.append(value)

    @possibilities.deleter
    def possibilities(self):
        self._possibilities.clear()

    def __str__(self):
        return f"{self._entry}, {self._possibilities}"


# Temp grid for now
grid = [
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)],
    [Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0), Entry(0)]
]


@Helper
def pprint(g):
    for i in range(3):
        print(
            f"{g[i][0].entry} {g[i][1].entry} {g[i][2].entry} | "
            f"{g[i][3].entry} {g[i][4].entry} {g[i][5].entry} | "
            f"{g[i][6].entry} {g[i][7].entry} {g[i][8].entry} | ")
    print(f"{'-'*23}")
    for i in range(3, 6):
        print(
            f"{g[i][0].entry} {g[i][1].entry} {g[i][2].entry} | "
            f"{g[i][3].entry} {g[i][4].entry} {g[i][5].entry} | "
            f"{g[i][6].entry} {g[i][7].entry} {g[i][8].entry} | ")
    print(f"{'-'*23}")
    for i in range(6, 9):
        print(
            f"{g[i][0].entry} {g[i][1].entry} {g[i][2].entry} | "
            f"{g[i][3].entry} {g[i][4].entry} {g[i][5].entry} | "
            f"{g[i][6].entry} {g[i][7].entry} {g[i][8].entry} | ")


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


@Test
def test():
    global grid
    import random
    for i in range(9):
        for j in range(9):
            grid[i][j].entry = random.randint(1, 9)
            grid[i][j].possibilities = random.randint(1, 9)
            grid[i][j].possibilities = random.randint(1, 9)
    pprint(grid)

    print(grid[0][0])
    del grid[0][0].possibilities
    grid[0][0].entry = 4
    print(grid[0][0])
    pprint(grid)


if __name__ == '__main__':
    test()
