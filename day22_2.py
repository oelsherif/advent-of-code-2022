with open("inputs/22.txt", "r") as File:
    grid = [line[:-1] for line in File]

def rotate(facing, dir):
    if dir == 'R':
        facing = (facing + 1) % 4
    elif dir == 'L':
        facing = (facing - 1) % 4
    return facing

def identify_face(x, y):
    for face, pos in top_left.items():
        x_start = pos[0]
        y_start = pos[1]
        if x in range(x_start, x_start + side) and y in range(y_start, y_start + side):
            return face


def next_tile_2(x, y, facing):
    dx, dy = deltas[facing]
    new_x = (x + dx) % width
    new_y = (y + dy) % height
    if grid[new_y][new_x] != ' ':
        return new_x, new_y, facing
    current_face = identify_face(x, y)
    x_start = top_left[current_face][0]
    y_start = top_left[current_face][1]
    x_face = x - x_start
    y_face = y - y_start
    if current_face == 1 and facing == 2:
        info = [5, 0, 0, n - y_face]
    elif current_face == 1 and facing == 3:
        info = [6, 0, 0, x_face]
    elif current_face == 2 and facing == 0:
        info = [4, 2, n, n - y_face]
    elif current_face == 2 and facing == 1:
        info = [3, 2, n, x_face]
    elif current_face == 2 and facing == 3:
        info = [6, 3, x_face, n]
    elif current_face == 3 and facing == 0:
        info = [2, 3, y_face, n]
    elif current_face == 3 and facing == 2:
        info = [5, 1, y_face, 0]
    elif current_face == 4 and facing == 0:
        info = [2, 2, n, n - y_face]
    elif current_face == 4 and facing == 1:
        info = [6, 2, n, x_face]
    elif current_face == 5 and facing == 2:
        info = [1, 0, 0, n - y_face]
    elif current_face == 5 and facing == 3:
        info = [3, 0, 0, x_face]
    elif current_face == 6 and facing == 0:
        info = [4, 3, y_face, n]
    elif current_face == 6 and facing == 1:
        info = [2, 1, x_face, 0]
    elif current_face == 6 and facing == 2:
        info = [1, 1, y_face, 0]

    new_face, new_facing, new_x_face, new_y_face = info
    new_x_start = top_left[new_face][0]
    new_y_start = top_left[new_face][1]
    new_x = new_x_start + new_x_face
    new_y = new_y_start + new_y_face
    return new_x, new_y, new_facing
            
#Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^). 
deltas = {
    0: [1, 0],
    1: [0, 1],
    2: [-1, 0],
    3: [0, -1]
}

#top left tile based on configuration:
## x12 #
## x3x #
## 54x #
## 6xx #
top_left = {
    1: [50, 0],
    2: [100, 0],
    3: [50, 50],
    4: [50, 100],
    5: [0, 100],
    6: [0, 150]
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

side = 50
n = 50 - 1

facing = 0
y = 0
x = grid[0].find('.')
for dir in dirs:
    if dir == 'L' or dir == 'R':
        facing = rotate(facing, dir)
        continue
    for i in range(dir):
        new_x, new_y, new_facing = next_tile_2(x, y, facing)
        if grid[new_y][new_x] == '#':
            break
        x, y, facing = new_x, new_y, new_facing

ans = 1000*(y+1) + 4*(x+1) + facing
print(ans)

