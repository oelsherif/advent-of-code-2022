with open("inputs/17.txt", "r") as File:
    line = File.readline()[:-1]

def generate_piece(x, y, index):
    temp = [pos[:] for pos in pieces[index]]
    #temp = pieces[index][:]
    for pos in temp:
        pos[0] += x
        pos[1] += y
    return temp
#print(line)
n = len(line) 

pieces = {
    0: [ [0, 0], [1, 0], [2, 0], [3, 0] ],
    1: [ [1, 0], [0, 1], [1, 1], [2, 1], [1, 2] ],
    2: [ [0, 0], [1, 0], [2, 0], [2, 1], [2, 2] ],
    3: [ [0, 0], [0, 1], [0, 2], [0, 3] ],
    4: [ [0, 0], [1, 0], [0, 1], [1, 1] ]
}

height = {0:0, 1:2, 2:2, 3:3, 4:1}

count = 0
i_piece = 0
max_count = 2022
tower_height = 0
grid = ["|.......|"] * 8000
grid = ["+-------+"] + grid

i_char = 0
for count in range(max_count):
    x = 3
    y = tower_height + 4
    flag = False
    while True:
        char = line[i_char]
        if char == '<':
            dx = -1
        else:
            dx = 1
        new_piece = generate_piece(x + dx, y, i_piece)
        for pos in new_piece:
            if grid[pos[1]][pos[0]] != '.':
                break
        else:
            x += dx
        new_piece = generate_piece(x, y-1, i_piece)
        for pos in new_piece:
            if grid[pos[1]][pos[0]] != '.':
                flag = True
                break
        else:
            y -= 1
        i_char = (i_char + 1) % n
        if flag:
            piece = generate_piece(x, y, i_piece)
            for pos in piece:
                row = grid[pos[1]]
                grid[pos[1]] = row[:pos[0]] + str(i_piece) + row[pos[0]+1:]
            tower_height = max(tower_height, y + height[i_piece])
            break 
    i_piece = (i_piece + 1) % 5
print(tower_height)