import Maze as m, Runner as r, Obstacle as o
def main():
    myMaze = m.Maze(10, 10)
    myMaze.createWalls()
    myMaze.createStart()
    myMaze.createFinish()
    myMaze.printMaze()

main()