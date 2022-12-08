f = open("inputs/7.txt", "r")
lines = f.readlines()
f.close()

sizes = {}
wd = []
for line in lines:
    words = line.split()
    if words[1] == 'cd':
        if words[2] == '..':
            wd.pop()
            path = '/'.join(wd)
        else:
            wd.append(words[2])
            path = '/'.join(wd)
            if path not in sizes:
                sizes[path] = 0
            else:
                print("ZZZZZZ")
    elif words[0].isnumeric():
        for i, dir in enumerate(wd):
            path = '/'.join(wd[:i+1])
            sizes[path] += int(words[0])

ans1 = 0
for key in sizes:
    if sizes[key] <= 100000:
        ans1 += sizes[key]

all_space = sizes['/']
needed = all_space - 40000000
min = all_space
for key in sizes:
    if sizes[key] > needed and sizes[key] < min:
        min = sizes[key]
        
print("part 1:")
print(ans1)
print("part 2:")
print(min)
