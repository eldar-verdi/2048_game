import random
import numpy as np
import pyxel


def swipe(row):
    while isFullyShifted(row) == False:
        shift(row)
    
    merge(row)

    while isFullyShifted(row) == False:
        shift(row)

    return row;
    
def merge(row):
    for i in range(len(row) - 1):
        if (row[i] == row[i + 1]):
            row[i] = row[i] * 2;
            row[i + 1] = 0
    
def isFullyShifted(row):
    nonZeroEncountered = False;
    for i in row:
        if (i != 0):
            nonZeroEncountered = True;
        if (i == 0):
            if (nonZeroEncountered):
                return False;
    return True;

def shift(row):
    for i in range(len(row) - 1):
        if (row[i + 1] == 0):
            row[i + 1] = row[i]
            row[i] = 0

def tests():
    row1 = [2,0,0,0]
    assert swipe(row1) == [0,0,0,2]

    row2 = [0,0,0,2]
    assert swipe(row2) == [0,0,0,2]

    row3 = [2,2,4,4]
    assert swipe(row3) == [0,0,4,8], f'expected: [0,0,4,8], actual = {row3}'

    row4 = [8,2,0,0]
    assert swipe(row4) == [0,0,8,2]

    row5 = [8,0,0,2]
    assert swipe(row5) == [0,0,8,2]

    row6 = [8,4,2,16]
    assert swipe(row6) == [8,4,2,16]

    row7 = [0,0,2,2]
    assert swipe(row7) == [0,0,0,4]

    row8 = [4,0,0,4]
    assert swipe(row8) == [0,0,0,8]

#tests()
    
def generate():
    firstNumberIndexX = random.randrange(0, 3)
    firstNumberIndexY = random.randrange(0, 3)

    grid = np.array([[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]]);

    grid[firstNumberIndexX, firstNumberIndexY] = 2
    #print(f'random index chosen = {firstNumberIndexX, firstNumberIndexY}')
    print(grid)
    return grid

def playMove(grid, direction):
    swipeDirection(grid, direction)
    addNewNumber(grid)

def swipeDirection(grid, direction):
    match direction:
        case 'right':
            for r in grid:
                swipe(r)
            return grid;
        case 'left':
            for r in grid:
                swipe(r[::-1])
            return grid;
        case 'down':
            for column in grid.T:
                swipe(column)
            return grid;
        case 'up':
            for column in grid.T:
                swipe(column[::-1])
            return grid;


def addNewNumber(grid):
    randomNewNumber = random.choice([2, 4])
    # the way this is generating sucks, we need to make it random, rather than adding in the first 0 value index it finds
    for r in grid:
        for c in range(len(r) - 1):
            if (r[c] == 0):
                grid[r[c]][c] = randomNewNumber
                return grid


def setupGame():
    gameGrid = generate()
    playMove(gameGrid, "right")
    print(gameGrid)
    playMove(gameGrid, "down")
    print(gameGrid)
    playMove(gameGrid, "left")
    print(gameGrid)
    playMove(gameGrid, "up")
    print(gameGrid)

setupGame()

# class App:
#     def __init__(self):
#         pyxel.init(160, 120)
#         # self.x = 0
#         # pyxel.run(self.update, self.draw)

#     # def update(self):
#     #     self.x = (self.x + 1) % pyxel.width

#     def draw(self):
#         pyxel.cls(0)
#         pyxel.rect(self.x, 0, 8, 8, 9)

# App()
