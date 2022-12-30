with open("inputs/24.txt", "r") as File:
    grid = [line[:-1] for line in File]

def move(bliz, dir):
    y, x = bliz
    dy, dx = deltas[dir]
    while True:
        x = (x + dx)%width
        y = (y + dy)%height
        if blank[y][x] == '.':
            return y, x

width = len(grid[0])
grid = ['#'*width] + grid
height = len(grid)
blank = []
for line in grid:
    blank.append(line.replace('>', '.').replace('<', '.').replace('^', '.').replace('v', '.'))

deltas = {
    '>': [0, 1],
    '<': [0, -1],
    '^': [-1, 0],
    'v': [1, 0]
}

blizzards = {'>': [], '<': [], '^': [], 'v': []}
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char in '><^v':
            blizzards[char].append([i, j])

current = [ [1, 1] ]
end_goal = [height-1, width - 2]
minute = 1
while True:
    new_grid = [line for line in blank]
    new_current = []
    for dir, arr in blizzards.items():
        for i, bliz in enumerate(arr):
            y, x = move(bliz, dir)
            arr[i] = [y, x]
            new_grid[y] = new_grid[y][:x] + 'x' + new_grid[y][x+1:]
    
    for pos in current:
        potentials = [pos]
        y, x = pos[0], pos[1]
        for dy, dx in deltas.values():
            potentials.append([y + dy, x + dx])
        for pot in potentials:
            if pot not in new_current and new_grid[pot[0]][pot[1]] == '.':
                new_current.append(pot)
    if end_goal in new_current:
        break
    current = [c[:] for c in new_current]
    minute += 1
print(minute)