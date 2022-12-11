with open("inputs/11.txt",'r') as file:
    lines = [line.replace(',', '').split() for line in file]

def worry(val, op):
    num1 = val
    if op[2] == 'old':
        num2 = val
    else:
        num2 = int(op[2])
    if op[1] == '+':
        return num1 + num2
    elif op[1] == '*':
        return num1 * num2

all_items = []
ops = []
test = []
for i, line in enumerate(lines):
    if line and line[0] == 'Monkey':
        all_items.append( [int(item) for item in lines[i+1][2:]])
        ops.append(lines[i+2][3:])
        nums = [lines[i+3][-1], lines[i+4][-1], lines[i+5][-1]]
        test.append( [int(num) for num in nums] )
n = len(all_items)
counts = [0 for k in range(n)]

#divisibility
product = 1
for i in range(n):
    product *= test[i][0]


rounds = 10000
for i in range(rounds):
    round_counts = [0 for k in range(n)]
    for j, items in enumerate(all_items):
        while items:
            num = items.pop(0)
            round_counts[j] += 1
            counts[j] += 1
            num = worry(num, ops[j])
            num %= product
            if num%test[j][0] == 0:
                dest = test[j][1]
            else:
                dest = test[j][2]
            all_items[dest].append(num)
    #print(round_counts)

counts.sort(reverse=True)
print("part 2:")
print(counts[0]*counts[1])
