from collections import defaultdict
with open("inputs/23.txt", "r") as File:
    grid = [line[:-1] for line in File]

elf_locs = defaultdict(lambda: 0)
elf_list = []
elf_count = 0
n = 10000
buffer = 2000
for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == '#':
            pos = (i + buffer)*n + (j + buffer)
            elf_list.append(pos)
            elf_locs[pos] = 1
            elf_count += 1

order = ["north", "south", "west", "east"]
elements = {
    "north": ["N", "NE", "NW"],
    "south": ["S", "SE", "SW"],
    "west": ["W", "NW", "SW"],
    "east": ["E", "NE", "SE"]
}
dir_val = {
    "N": -n,
    "NE": -n + 1,
    "E": 1,
    "SE": n + 1,
    "S": n,
    "SW": n - 1,
    "W": -1,
    "NW": -n - 1 
}

rounds = 10**6 #Set to 10 for part 1
for round in range(rounds):
    flag = False
    elf_prop = defaultdict(lambda: 0)
    prop_locs = defaultdict(lambda: 0)
    for elf in elf_list:
        elf_dir = {}
        for dir in dir_val:
            elf_dir[dir] = elf_locs[elf + dir_val[dir]]
        elf_gen = {
            "north": sum([elf_dir[d] for d in elements["north"]]),
            "south": sum([elf_dir[d] for d in elements["south"]]),
            "west": sum([elf_dir[d] for d in elements["west"]]),
            "east": sum([elf_dir[d] for d in elements["east"]])
        }
        if sum(list(elf_gen.values())) == 0:
            continue
        for dir in order:
            if elf_gen[dir] == 0:
                proposed = elf + dir_val[elements[dir][0]]
                elf_prop[elf] = proposed
                prop_locs[proposed] += 1
                break
    
    for elf, proposed in elf_prop.items():
        if prop_locs[proposed] == 1:
            flag = True
            elf_list.remove(elf)
            elf_list.append(proposed)
            elf_locs[elf] = 0
            elf_locs[proposed] = 1
    order.append(order.pop(0))
    if not flag:
        break

xs = [pos%n for pos in elf_list]
ys = [pos//n for pos in elf_list]
print(f"Number of rounds is {round + 1}")
# for i in range(len(xs)):
#     print (xs[i]-min(xs), ys[i] - min(ys))

ans = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - elf_count
print(f"Number of empty tiles is: {ans}")