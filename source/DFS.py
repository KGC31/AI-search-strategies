#DFS implementation
def DFS(maze, visited, path, root, end):
    if end in visited:
        return
    else:
        if root not in visited:
            visited.append(root)
            for neighbour in maze[root]:
                DFS(maze, visited, path, neighbour[0], end)
            if end in visited:
                path.append(root)