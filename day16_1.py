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

instances['AA'] = [ [0, set()] ]
minutes = 30
for minute in range(minutes):
    new_insts = {}
    for key in instances:
        for instance in instances[key]:
            released = instance[0]
            tbr = 0
            for open_valve in instance[1]:
                tbr += rates[open_valve]
            released += tbr
            new_inst = [released, instance[1]]
            if rates[key]:
                temp = instance[1].copy()
                temp.add(key)
                rare_inst = [released, temp]
                new_insts = add_inst(key, rare_inst, new_insts)                
            else:
                news_insts = add_inst(key, new_inst, new_insts)
            for neighbor in neighbors[key]:
                new_insts = add_inst(neighbor, new_inst, new_insts)
    instances = new_insts.copy()

#print(instances)
nums = []
for key in instances:
    for inst in instances[key]:
        nums.append(inst[0])
print(max(nums))
