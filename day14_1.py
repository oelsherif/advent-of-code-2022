with open("inputs/14.txt", "r") as File:
    lines = File.readlines()

def give_range(co1, co2):
    arr = []
    x1, y1 = co1
    x2, y2 = co2
    if x1 == x2:
        y1, y2 = min(y1, y2), max(y1, y2)
        for i in range(y1, y2+1):
            arr.append([x1, i])
    elif y1 == y2:
        x1, x2 = min(x1, x2), max(x1, x2)
        for i in range(x1, x2+1):
            arr.append([i, y1])
    return arr



for i, line in enumerate(lines):
    line = line.replace('-','').replace('>','').split()
    for j, word in enumerate(line):
        word = [int(num) for num in word.split(',')]
        line[j] = word
        #print(word)
    lines[i] = line

max_x = 0
min_x = 1000000
max_y = 0
min_y = 1000000
for line in lines:
    for word in line:
        x = word[0]
        y = word[1]
        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y
width = max_x - min_x + 3
height = max_y + 2
grid = [ '.'*width for i in range(height)]
start_x = 500 - min_x + 1
start_y = 0
grid[start_y] = grid[start_y][:start_x] + '+' + grid[start_y][start_x+1:]
for i, line in enumerate(lines):
    for j, word1 in enumerate(line[:-1]):
        word2 = line[j+1]
        arr = give_range(word1, word2)
        for co in arr:
            x, y = co[0] - min_x + 1, co[1]
            grid[y] = grid[y][:x] + '#' + grid[y][x+1:]

units = 0
while True:
    x = start_x
    for y in range(height - 1):
        if grid[y+1][x] == '.':
            continue
        if grid[y+1][x-1] == '.':
            x -= 1
            continue
        if grid[y+1][x+1] == '.':
            x += 1
            continue
        grid[y] = grid[y][:x] + 'o' + grid[y][x+1:]
        break
    else:
        break
    units += 1

for line in grid:
    print(line)
print(units)