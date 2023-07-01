#Get data from maze.txt
def inputMaze(filename):
    try:
        f = open(filename, "r")
        maze = {}
        size = int(f.readline())
        size = pow(size, 2)
        start = int(f.readline())
        end = int(f.readline())

        for i in range (0, size):
            maze[i] = []
            txt = f.readline()
            list = txt.split("/ ")
            for j in range (len(list)):
                list[j] = eval(list[j])
                maze[i].append(list[j])
        f.close()
        return maze, size, start, end
    
    except FileNotFoundError:
        return None, None, None, None