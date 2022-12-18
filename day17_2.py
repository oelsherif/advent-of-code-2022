import time

with open("inputs/test17.txt", "r") as File:
    line = File.readline()[:-1]

def generate_piece(x, y, index):
    temp = [pos[:] for pos in pieces[index]]
    for pos in temp:
        pos[0] += x
        pos[1] += y
    return temp
n = len(line) 

pieces = {
    0: [ [0, 0], [1, 0], [2, 0], [3, 0] ],
    1: [ [1, 0], [0, 1], [1, 1], [2, 1], [1, 2] ],
    2: [ [0, 0], [1, 0], [2, 0], [2, 1], [2, 2] ],
    3: [ [0, 0], [0, 1], [0, 2], [0, 3] ],
    4: [ [0, 0], [1, 0], [0, 1], [1, 1] ]
}

height = {0:0, 1:2, 2:2, 3:3, 4:1}

i_piece = 0
max_count = 2000
tower_height = 0
grid = ["|.......|"] * int(max_count*1.6)
grid = ["+-------+"] + grid
store = []
start_time = time.time()
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
                grid[pos[1]] = row[:pos[0]] + '#' + row[pos[0]+1:]
            tower_height = max(tower_height, y + height[i_piece])
            break 
    i_piece = (i_piece + 1) % 5
    if i_char == 3:
        store.append([count, tower_height])
    if count == 1440:
        print(tower_height)
end_time = time.time()
#for i in range(len(store)-1):
#    print (store[i])

#By printing the counts and tower height at a certain character everytime:
#pattern: every 1720 counts, height increases by 2729
#ran to get height at 1000000000000%1720, then add the increase in every 1720 cycle
print(f"Runtime = {end_time - start_time} seconds")

big = 1000000000000
div = big//1720
remainder = big%1720
print( 2230 + div*2729 - 1)
