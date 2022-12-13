with open("inputs/12.txt",'r') as file:
    lines = [line[:-1] for line in file]

def value(char):
    if char == 'S':
        return value('a')
    elif char == 'E':
        return value('z')
    else:
        return ord(char) - ord('a')

m = len(lines)
n = len(lines[0])
next = []
mat = [ [0]*n for i in range(m)]
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        #if char == 'S':     #USE THIS CONDITION FOR PART 1
        if value(char) == value('S'):
            start = [i, j]
            next.append(start)
            mat[i][j] = 1

step = 0
while(True):
    current = next[:]
    next = []
    for p in current:
        y, x = p[0], p[1]
        alt = value(lines[y][x])
        if alt == value('E'):
            break
        candidates = []
        candidates.append([max(y-1, 0), x])
        candidates.append([min(y+1, m-1), x])
        candidates.append([y, max(x-1, 0)])
        candidates.append([y, min(x+1, n-1)])
        for cand in candidates:
            new_y, new_x = cand[0], cand[1]
            new_alt = value(lines[new_y][new_x])
            is_visited = mat[new_y][new_x]
            if (new_alt <= alt + 1) and (not is_visited):
                next.append( cand )
                mat[new_y][new_x] = 1
    if alt == value('E'):
        break
    step += 1
    
print(step)

