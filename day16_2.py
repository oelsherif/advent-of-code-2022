import time

with open("inputs/16.txt", "r") as File:
    lines = File.readlines()

rates = {}
neighbors = {}
instances = {}

def add_inst(valve, new_inst, dict):
    if valve not in dict:
        dict[valve] = [new_inst]
    else:
        pr_new = new_inst[0]
        opens_new = new_inst[1]
        flag = 1
        i = 0
        while i < len(dict[valve]):
            old_inst = dict[valve][i]
            pr_old = old_inst[0]
            opens_old = old_inst[1]
            if pr_new <= pr_old and opens_new.issubset(opens_old):
                flag = 0
                break
            elif pr_old <= pr_new and opens_old.issubset(opens_new):
                dict[valve].pop(i)
                continue
            else:
                i += 1
        if flag:
            dict[valve].append(new_inst)
    return dict

def long_key(key1, key2):
    k = [key1, key2]
    k.sort()
    k = ''.join(k)
    return k

for line in lines:
    line = line.split()
    valve = line[1]
    flow_rate = int(line[4].replace('rate=', '').replace(';', ''))
    adjacents = []
    for word in line[9:]:
        adjacents.append(word.replace(',', ''))
    rates[valve] = flow_rate
    neighbors[valve] = adjacents
    instances[valve] = []

instances['AAAA'] = [ [0, set()] ]
minutes = 26

start_time = time.time()

for minute in range(minutes):
    new_insts = {}
    for key in instances:
        key1 = key[:2]
        key2 = key[2:]
        for instance in instances[key]:
            released = instance[0]
            tbr = 0
            open_valves = instance[1]
            for open_valve in open_valves:
                tbr += rates[open_valve]
            released += tbr
            new_inst = [released, open_valves]

            if rates[key1] and rates[key2]:
                temp = open_valves.copy()
                temp.add(key1)
                temp.add(key2)
                rare_inst = [released, temp]
                new_insts = add_inst(key, rare_inst, new_insts)                
            if rates[key1]:
                for neighbor in neighbors[key2]:
                    temp = open_valves.copy()
                    temp.add(key1)
                    new_key = long_key(key1, neighbor)
                    rare_inst = [released, temp]
                    new_insts = add_inst(new_key, rare_inst, new_insts)
            if rates[key2]:
                for neighbor in neighbors[key1]:
                    temp = open_valves.copy()
                    temp.add(key2)
                    new_key = long_key(key2, neighbor)
                    rare_inst = [released, temp]
                    new_insts = add_inst(new_key, rare_inst, new_insts)
            for neighbor1 in neighbors[key1]:
                for neighbor2 in neighbors[key2]:
                    new_key = long_key(neighbor1, neighbor2)
                    new_insts = add_inst(new_key, new_inst, new_insts)

    instances = new_insts.copy()

#print(instances)
nums = []
for key in instances:
    for inst in instances[key]:
        nums.append(inst[0])

end_time = time.time()
print(f"Runtime = {end_time - start_time}")
print(max(nums))

