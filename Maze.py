import random
import math

class Maze:

    def __init__(self, x_size, y_size):
        self.mazeArray = [[" " for y in range(y_size)] for x in range(x_size)]
        self.width = x_size
        self.height = y_size
        self.start = None
        self.startChar = "S"
        self.finish = None
        self.finishChar = "F"

    # GETTER AND SETTER METHODS ---------------------------------------------------------------------------------------

    def getStart(self):
        return self.start

    # Set the start value to a given position
    def setStart(self, x, y):
        # If a start already exists, remove it from the array
        if (self.start != None):
            self.mazeArray[self.start[0]][self.start[1]] = " "

        if (self.mazeArray[x][y] == " "):
            self.start = (x,y)
            self.mazeArray[x][y] = self.startChar
            return True
        else:
            return False

    def getFinish(self):
        return self.finish

    # Set the finish value to a given position
    def setFinish(self, x, y):
        # If a finish already exists, remove it from the array
        if (self.finish != None):
            self.mazeArray[self.finish[0]][self.finish[1]] = " "

        if (self.mazeArray[x][y] == " "):
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
        for y in range(self.height):
            self.mazeArray[0][y] = "│"
            self.mazeArray[self.width - 1][y] = "│"

        for x in range(self.width):
            self.mazeArray[x][0] = "-"
            self.mazeArray[x][self.height - 1] = "-"

        # Applying ASCII corners to array
        self.mazeArray[0][0] = "╔"
        self.mazeArray[self.width - 1][0] = "╗"
        self.mazeArray[0][self.height - 1] = "╚"
        self.mazeArray[self.width - 1][self.height - 1] = "╝"

    # Randomly set the start to somewhere within the maze, that's not on a wall or collides with an obstacle
    def createStart(self):
        while (True):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if self.setStart(x,y):
                break

    # Randomly set the finish to somewhere within the maze, that's not on a wall or collides with an obstacle
    def createFinish(self):
        while (True):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if self.setFinish(x, y):
                break

    # Print out the entire maze array
    def printMaze(self):
        for y in range(self.height):
            print()
            for x in range(self.width):
                print(self.mazeArray[x][y], end="")
