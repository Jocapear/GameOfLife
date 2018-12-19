#Rules
#Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by overpopulation.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

#Principles
# There should be no explosive growth.
# There should exist small initial patterns with chaotic, unpredictable outcomes.
# There should be potential for von Neumann universal constructors.
# The rules should be as simple as possible, whilst adhering to the above constraints.

import numpy as np
import time

class World:
    def __init__(self):
        self.space = []
        self.size = 0

    def show(self):
        print(self.space)
        print("----------------------")

    def initialize(self, gameSize):
        self.space = np.zeros((gameSize, gameSize))
        self.size = gameSize
        self.space[1][1] = 1
        self.space[1][2] = 1
        self.space[1][3] = 1
        self.space[10][10] = 1
        self.space[10][9] = 1
        self.space[10][11] = 1
        self.space[8][10] = 1
        self.space[9][11] = 1

    def modify(self, newSpace, i, j, aliveNeighbors):
        #Rules can be modified here
        #Rule 1: Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        if aliveNeighbors < 2:
            newSpace[i][j] = 0
        #Rule 2: Any live cell with two or three live neighbors lives on to the next generation.
        elif newSpace[i][j] and (aliveNeighbors == 2 or aliveNeighbors == 3):
            newSpace[i][j] = 1
        #Rule 3: Any live cell with more than three live neighbors dies, as if by overpopulation.
        elif newSpace[i][j] and aliveNeighbors > 3:
            newSpace[i][j] = 0
        #Rule 4: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        elif not newSpace[i][j] and aliveNeighbors == 3:
            newSpace[i][j] = 1

    def findAliveNeighbors(self,i,j):
        lives = 0
        if i>0 and j>0 and self.space[i-1][j-1]: #Top-left
            lives += 1
            # print("1")
        if i>0 and self.space[i-1][j]: #Top-mid
            lives += 1
            # print("2")
        if (i>0 and j<self.size-1) and self.space[i-1][j+1]: #Top-right
            lives += 1
            # print("3")
        if j>0 and self.space[i][j-1]: #Mid-left
            lives += 1
            # print("4")
        if j<self.size-1 and self.space[i][j+1]: #Mid-right
            lives += 1
            # print("5")
        if (j>0 and i<self.size-1) and self.space[i+1][j-1] == 1: #Bot-left
            lives += 1
            # print("6")
        if i<self.size-1 and self.space[i+1][j]: #Bot-mid
            lives += 1
            # print("7")
        if (i<self.size-1 and j<self.size-1) and self.space[i+1][j+1]: #Bot-right
            lives += 1
            # print("8")

        #print("i = " + str(i) + ", j = " + str(j) + ", Neighbors = " + str(lives))
        return lives

    def nextFrame(self):
        futureFrame = self.space.copy()
        for row in range(self.size):
            for col in range(self.size):
                aliveNeighbors = self.findAliveNeighbors(row, col)
                # print(str(row) + " " + str(col))
                self.modify(futureFrame, row, col, aliveNeighbors)
        self.space = futureFrame

def main():
    gameSize = 20
    world = World()
    world.initialize(gameSize)
    world.show()
    while True:
        time.sleep(.2)
        world.nextFrame()
        world.show()
if __name__ == "__main__":
    main()
    