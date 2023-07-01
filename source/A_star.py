import math 

def h(cell, end):
    x_cell = cell / 10
    y_cell = cell % 10
    x_end = end / 10
    y_end = end % 10

    return abs(x_end - x_cell) + abs(y_end - y_cell)

def g(maze, root, neighbour):
    for i in maze[root]:
        if i[0] == neighbour:
            cost = i[1]
    return cost

def A_star(maze, visited, path, root, end):
    if end in visited:
        return
    else:
        if root not in visited:
            queue = []
            visited.append(root)
            for neighbour in maze[root]:
                queue.append(int(h(neighbour[0], end)) + int(g(maze, root, neighbour[0])))
            
            for 

            A_star(maze, visited, path, maze[root][queue.index(min(queue))][0], end)
            if end in visited:
                path.append(root)
