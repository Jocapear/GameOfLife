from graphics import *
from world import World

def showFrame(win, winSize, space, spaceSize):
    pixelSize = winSize//spaceSize
    for i in range(spaceSize):
        for j in range(spaceSize):
            pixel = Rectangle(Point(j*pixelSize,i*pixelSize), Point((j*pixelSize)+pixelSize, (i*pixelSize)+pixelSize))
            if space[i][j]:
                pixel.setFill("white")
            else:
                pixel.setFill("black")
            pixel.draw(win)
    update()

def main():
    world = World()
    gameSize = 100
    windowSize = 700
    world.initialize(gameSize)
    win = GraphWin('Game', windowSize, windowSize, autoflush=False) # give title and dimensions
    while True:
        #time.sleep(.2)
        world.nextFrame()
        showFrame(win, windowSize, world.space, world.size)
    win.getMouse()
    win.close()

main()
