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


rounds = 20
for i in range(rounds):
    for j, items in enumerate(all_items):
        while items:
            num = items.pop(0)
            counts[j] += 1
            num = worry(num, ops[j])
            num //= 3
            if num%test[j][0] == 0:
                dest = test[j][1]
            else:
                dest = test[j][2]
            all_items[dest].append(num)

counts.sort(reverse=True)
print("part 1:")
print(counts[0]*counts[1])
