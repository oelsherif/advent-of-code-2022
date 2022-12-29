with open("inputs/22.txt", "r") as File:
    grid = [line[:-1] for line in File]

def rotate(facing, dir):
    if dir == 'R':
        facing = (facing + 1) % 4
    elif dir == 'L':
        facing = (facing - 1) % 4
    return facing

def next_tile(x, y, facing):
    dx, dy = deltas[facing]
    new_x, new_y = x, y
    while True:
        new_x = (new_x + dx) % width
        new_y = (new_y + dy) % height
        if grid[new_y][new_x] != ' ':
            return new_x, new_y
            
#Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). 
deltas = {
    0: [1, 0],
    1: [0, 1],
    2: [-1, 0],
    3: [0, -1]
}
s = grid.pop()
grid.pop()
height = len(grid)
width = max([len(line) for line in grid])

for i, line in enumerate(grid):
    if len(line) < width:
        grid[i] += (' ' * (width-len(line)))

dirs = []
while s:
    char = s[0]
    if char in "LR":
        dirs.append(char)
        s = s[1:]
        continue
    for i, char in enumerate(s):
        if char in "LR":
            dirs.append(int(s[:i]))
            s = s[i:]
            break
    if 'L' not in s and 'R' not in s:
        dirs.append(int(s))
        break

facing = 0
y = 0
x = grid[0].find('.')
for dir in dirs:
    if dir == 'L' or dir == 'R':
        facing = rotate(facing, dir)
        continue
    for i in range(dir):
        new_x, new_y = next_tile(x, y, facing)
        if grid[new_y][new_x] == '#':
            break
        x, y = new_x, new_y

ans = 1000*(y+1) + 4*(x+1) + facing
print(ans)