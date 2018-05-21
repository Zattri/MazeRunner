import random
import math

class Maze:

    def __init__(self, mazeWidth, mazeHeight):
        self.mazeArray = [[" " for y in range(mazeHeight)] for x in range(mazeWidth)]
        self.width = mazeWidth
        self.height = mazeHeight
        self.start = None
        self.startChar = "S"
        self.finish = None
        self.finishChar = "F"

    # GETTER AND SETTER METHODS ---------------------------------------------------------------------------------------

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getStart(self):
        return self.start

    # Set the start value to a given position
    def setStart(self, x, y):
        if self.mazeArray[x][y] == " ":
            if self.start:
                self.mazeArray[self.start[0]][self.start[1]] = " "
            self.start = (x,y)
            self.mazeArray[x][y] = self.startChar
            return True
        else:
            return False

    def getFinish(self):
        return self.finish

    # Set the finish value to a given position
    def setFinish(self, x, y):
        if self.mazeArray[x][y] == " ":
            if self.finish:
                self.mazeArray[self.finish[0]][self.finish[1]] = " "
            self.finish = (x, y)
            self.mazeArray[x][y] = self.finishChar
            return True
        else:
            return False

    def setCell(self, x, y, char):
        self.mazeArray[x][y] = char

    # -----------------------------------------------------------------------------------------------------------------

    # Fill the border of the array with characters to represent walls
    def createWalls(self):
        for y in range(1, self.height - 1):
            self.mazeArray[0][y] = "│"
            self.mazeArray[self.width - 1][y] = "│"

        for x in range(1, self.width - 1):
            self.mazeArray[x][0] = "-"
            self.mazeArray[x][self.height - 1] = "-"

        # Applying ASCII corners to array
        self.mazeArray[0][0] = "╔"
        self.mazeArray[self.width - 1][0] = "╗"
        self.mazeArray[0][self.height - 1] = "╚"
        self.mazeArray[self.width - 1][self.height - 1] = "╝"

    # Randomly set the start to somewhere within the maze, that's not on a wall or collides with an obstacle
    def createStart(self):
        while True:
            x = random.randint(2, self.width - 3)
            y = random.randint(self.height/2, self.height - 2)
            if self.setStart(x,y):
                break

    # Randomly set the finish to somewhere within the maze, that's not on a wall or collides with an obstacle
    def createFinish(self):
        while True:
            x = random.randint(2, self.width - 2)
            y = random.randint(2, self.height/2 - 3)
            if self.setFinish(x, y):
                break

    # Print out the entire maze array
    def printMaze(self):
        for y in range(self.height):
            print()
            for x in range(self.width):
                print(self.mazeArray[x][y], end="")
        print()

    # Return if a cell is empty or not, True for empty
    def checkEmpty(self, cell):
        return self.mazeArray[cell[0]][cell[1]] == " "

    # Return if a cell is in a 2x2 grid near a corner
    def checkCorner(self, cell):
        # Make a list of corners and compare the cell against that
        # Come up with a check that registers is a start or finish blocks an obstacle in the corner by a wall
        return False