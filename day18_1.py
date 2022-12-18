with open("inputs/18.txt", "r") as File:
    pixels = [ [int(word) for word in line[:-1].split(",") ] for line in File]

def blank_neighbors(p):
    x = p[0] + 1
    y = p[1] + 1
    z = p[2] + 1
    c = 0
    c += grid[x][y][z-1] + grid[x][y][z+1]
    c += grid[x][y-1][z] + grid[x][y+1][z]
    c += grid[x-1][y][z] + grid[x+1][y][z]
    return c

n = len(pixels)
#xs = [pixel[0] for pixel in pixels]
#ys = [pixel[1] for pixel in pixels]
#zs = [pixel[2] for pixel in pixels]
#print(min(xs), max(xs))
#print(min(ys), max(ys)) ####range 1-6 for each coordinate in test
#print(min(zs), max(zs)) ####range 0-19 for each coordinate in real dataset

side = 22
grid = [[[1]*side for i in range(side)] for j in range(side)]
for p in pixels:
    grid[p[0] + 1][p[1] + 1][p[2] + 1] = 0

count = 0
for p in pixels:
    count += blank_neighbors(p)

print(count)