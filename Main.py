import Maze as m, Runner as r, Obstacle as o
def main():
    myMaze = m.Maze(12, 12)
    myMaze.createWalls()
    myMaze.createStart()
    myMaze.createFinish()
    myObstacle = o.Obstacle(myMaze, 20, False)
    myObstacle.generateObstacle()
    myMaze.printMaze()
    myObstacle.printPath()
    print("Generation Complete")

main()