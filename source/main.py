import time
from file_handle import *
from DFS import DFS
from BFS import BFS
from A_star import A_star


#--------------------------Main-----------------------------
maze = {}
size, start, end = 0, 0, 0
maze, size, start, end = inputMaze("maze.txt")


# BFS
visited = []
path = []
print("===BFS===")
start_time = time.time()
BFS(maze, visited, path, start, end)
print("- Visited list:\n", visited)
path.reverse()
print("- Solution path:\n", path)
end_time = time.time()
print("- Execution time:", (end_time - start_time)*10**3, "ms")

#DFS
visited = []
path = []
print("===DFS===")
start_time = time.time()
DFS(maze, visited, path, start, end)
end_time = time.time()
print("- Visited list:\n", visited)
path.reverse()
print("- Solution path:\n", path)
print("- Execution time:", (end_time - start_time)*10**3, "ms")

# A* search
visited = []
path = []
print("===A*===")
start_time = time.time()
A_star(maze, visited, path, start, end)
end_time = time.time()
print("- Visited list:\n", visited)
path.reverse()
print("- Solution path:\n", path)
print("- Execution time:", (end_time - start_time)*10**3, "ms")