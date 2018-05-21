import random
class Obstacle:
    def __init__(self, parentMaze, objectLength, wallConnection):
        self.maze = parentMaze
        self.length = objectLength
        self.connection = wallConnection
        self.obstacleChar = "^"
        self.path = []
        # A path is a series of connected cells that make up an obstacle
        self.w = self.maze.getWidth()
        self.h = self.maze.getHeight()

    # Add a cell to the path of an obstacle
    def addToPath(self, cell):
        # Maybe change this and use the length to recursively add adjacent cells instead
        if len(self.path) < self.length:
            self.path.append(cell)

    # Select a cell next to a wall to start an obstacle at
    def pickStartLocation(self):
        if (self.connection):
            # Decide which wall the obstacle connects to
            wall = random.randint(0,3)
            if wall == 0: # Top
                x = random.randint(2, self.w - 3)
                y = 1
            elif wall == 1: # Left
                x = 1
                y = random.randint(2, self.h - 3)
            elif wall == 2: # Right
                x = self.w - 2
                y = random.randint(2, self.h - 3)
            elif wall == 3: # Bottom
                x = random.randint(2, self.w - 3)
                y = self.h - 2

        # Spawn the original point of the wall connected obstacle away from an S or F marker

        else:
            x = random.randint(2, self.w - 3)
            y = random.randint(2, self.h - 3)

        self.path.append((x,y))

    # Returns whether there are walls adjacent to the cell, True for near wall
    def checkNearWall(self, cell):
        if (cell[0] in range(2, self.w - 2)) & (cell[1] in range (2, self.h - 2)):
            return False
        else:
            return True

    def generateObstacle(self):
        self.pickStartLocation()
        for x in range(1, self.length):
            latestCell = self.path[-1]

            #Debugging
            # - print(self.path)
            # - self.maze.printMaze()

            while True:
                direction = random.randint(0,3)
                if direction == 0: # Up
                    newCell = (latestCell[0], latestCell[1] - 1)
                elif direction == 1:  # Left
                    newCell = (latestCell[0] - 1, latestCell[1])
                elif direction == 2:  # Right
                    newCell = (latestCell[0] + 1, latestCell[1])
                elif direction == 3:  # Down
                    newCell = (latestCell[0], latestCell[1] + 1)
                if (not self.checkNearWall(newCell)) & self.maze.checkEmpty(newCell): # Need to also check if an obstacle is touching another obstacle
                    self.addToPath(newCell)
                    self.maze.setCell(newCell[0], newCell[1], self.obstacleChar)
                    break

    # For debugging
    def printPath(self):
        print("--------------")
        print("Obstacle path")
        for cell in self.path:
            print(str(cell[0])+","+str(cell[1]))
        print("--------------")