from maze import Maze
from maze import Solver

m = Maze.generate(5, 5)
print(Solver.solve(m, (0, 0), (4, 4)))