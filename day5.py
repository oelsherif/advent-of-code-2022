f = open("inputs/5.txt", "r")
lines = f.readlines()
f.close()

size = len(lines[0])//4
towers1 = [ [] for i in range(size)]
towers2 = [ [] for i in range(size)]

for line in lines:
    if line[1] == '1':
        break
    for i in range(size):
        pos = 4*i + 1
        if line[pos] != ' ':
            towers1[i] = [line[pos]] + towers1[i]
            towers2[i] = [line[pos]] + towers2[i]


start, end = lines.index('\n') + 1, len(lines) 
for i in range(start, end):
    line = lines[i]
    items = line.split()
    qnt = int(items[1])
    source = int(items[3]) - 1
    destination = int(items[5]) - 1

    ####part1
    for i in range(qnt):
        towers1[destination].append(towers1[source].pop())

    ####part2
    towers2[destination] += towers2[source][-qnt:]
    towers2[source] = towers2[source][:-qnt]
ans1 = ''.join([tower[-1] for tower in towers1])
ans2 = ''.join([tower[-1] for tower in towers2])


print("part 1:")
print(ans1)
print("part 2:")
print(ans2)    
