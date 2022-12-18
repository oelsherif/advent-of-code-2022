with open("inputs/18.txt", "r") as File:
    pixels = [ [int(word) + 1 for word in line[:-1].split(",") ] for line in File]
    # added the +1 in the beginning to pad the grid and not worry about boundaries later

def blank_neighbors(p):
    c = 0
    for neighbor in neighbors(p):
        x = neighbor[0]
        y = neighbor[1]
        z = neighbor[2]
        c += grid[x][y][z]
    return c

def neighbors(p):
    x = p[0]
    y = p[1]
    z = p[2]
    neighbor_list = []
    neighbor_list += [ [x, y, max(0, z-1)], [x, y, min(side-1, z+1)]]
    neighbor_list += [ [x, max(0, y-1), z], [x, min(side-1, y+1), z]]
    neighbor_list += [ [max(0, x-1), y, z], [min(side-1, x+1), y, z]]
    return(neighbor_list)

n = len(pixels)

#side = 9 #for test
side = 22
grid = [[[0]*side for i in range(side)] for j in range(side)] #set all points to zero
for p in pixels:
    grid[p[0]][p[1]][p[2]] = -1 #set all lava cubes to -1
for i in range(side): #set all edges to 1
    grid[0][0][i] = 1
    grid[0][-1][i] = 1
    grid[-1][0][i] = 1
    grid[-1][-1][i] = 1
    grid[0][i][0] = 1
    grid[0][i][-1] = 1
    grid[-1][i][0] = 1
    grid[-1][i][-1] = 1
    grid[i][0][0] = 1
    grid[i][0][-1] = 1
    grid[i][-1][0] = 1
    grid[i][-1][-1] = 1

flag = True
while(flag):  #spread everything on the outside to 1
    flag = False
    for i in range(side):
        for j in range(side):
            for k in range(side):
                p = [i, j, k]
                if grid[i][j][k] != 1:
                    continue
                for neighbor in neighbors(p):
                    x = neighbor[0]
                    y = neighbor[1]
                    z = neighbor[2]
                    if grid[x][y][z] == 0:
                        grid[x][y][z] = 1
                        flag = True
for p in pixels:
    grid[p[0]][p[1]][p[2]] = 0 #now everything but the outside should be 0

count = 0
for p in pixels:
    count += blank_neighbors(p)

print(count)