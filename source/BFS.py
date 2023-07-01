#BFS implementation
def BFS(maze, visited, path, root, end):
    queue = []
    queue.append(root)
    visited.append(root)
    path.append(end)

    while queue and end not in visited:
        m = queue.pop(0)
        
        for neighbour in maze[m]:
            if neighbour[0] not in visited:
                visited.append(neighbour[0])
                queue.append(neighbour[0])

    dict = {}
    for i in maze:
        dict[i] = []
        for j in range (0, len(maze[i])):
            dict[i].append(maze[i][j][0])
 
    while root not in path:
        for i in visited:
            if path[len(path) - 1] in dict[i]:
                path.append(i)
                break
                
