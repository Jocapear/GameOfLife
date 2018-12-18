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
        self.space[1][1] = 1
        self.space[1][2] = 1
        self.space[1][3] = 1

    def modify(self, i,j,aliveNeighbors):
        #Rules can be modified here
        #Rule 1: Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        if aliveNeighbors < 2:
            self.space[i][j] = 0
        #Rule 2: Any live cell with two or three live neighbors lives on to the next generation.
        elif self.space[i][j] and (aliveNeighbors == 2 or aliveNeighbors == 3):
            self.space[i][j] = 1
        #Rule 3: Any live cell with more than three live neighbors dies, as if by overpopulation.
        elif self.space[i][j] and aliveNeighbors > 3:
            self.space[i][j] = 0
        #Rule 4: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        elif not self.space[i][j] and aliveNeighbors == 3:
            self.space[i][j] = 1

    def findAliveNeighbors(self,i,j):
        lives = 0
        if self.space[i-1][j-1] and i>0 and j>0: #Top-left
            lives += 1
        if self.space[i-1][j] and i>0: #Top-mid
            lives += 1
        if self.space[i-1][j+1] and i>0 and j<self.size-1: #Top-right
            lives += 1
        if self.space[i][j-1] and j>0: #Mid-left
            lives += 1
        if self.space[i][j+1] and j<self.size-1: #Mid-right
            lives += 1
        if self.space[i+1][j-1] and i<self.size-1 and j>0 : #Bot-left
            lives += 1
        if self.space[i+1][j] and i<self.size-1: #Bot-mid
            lives += 1
        if self.space[i+1][j+1] and i<self.size-1 and j<self.size-1: #Bot-right
            lives += 1
        return lives

    def nextFrame(self):
        for row in range(self.size):
            for col in range(self.size):
                aliveNeighbors = self.findAliveNeighbors(row, col)
                self.modify(row,col,aliveNeighbors)

def main():
    gameSize = 5
    world = World()
    world.initialize(gameSize)
    world.show()
    while True:
        time.sleep(1)
        world.nextFrame()
        world.show()
if __name__ == "__main__":
    main()