
class Obstacle:
    def __init__(self, parentMaze, objectLength):
        self.maze = parentMaze
        self.length = objectLength
        self.path = []
        # A path is a series of connected cells that make up an obstacle



    # Add a cell to the path of an obstacle
    def addToPath(self, cell):
        # Maybe change this and use the length to recursively add adjacent cells instead
        if (len(self.path) < self.length):
            self.path.append(cell)

    # Select a cell next to a wall to start an obstacle at
    def pickStartWall(self):
        w = self.maze.getWidth()
        h = self.maze.getHeight()