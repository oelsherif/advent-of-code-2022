with open("inputs/test11.txt",'r') as file:
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

all_items_1 = []
ops = []
test = []
for i, line in enumerate(lines):
    if line and line[0] == 'Monkey':
        all_items_1.append( [int(item) for item in lines[i+1][2:]])
        ops.append(lines[i+2][3:])
        nums = [lines[i+3][-1], lines[i+4][-1], lines[i+5][-1]]
        test.append( [int(num) for num in nums] )
n = len(all_items_1)
all_items_2 = [items[:] for items in all_items_1]
counts_1 = [0 for i in range(n)]
counts_2 = [0 for i in range(n)]


rounds_1 = 20
for i in range(rounds_1):
    for j, items in enumerate(all_items_1):
        while items:
            num = items.pop(0)
            counts_1[j] += 1
            num = worry(num, ops[j])
            num //= 3
            if num%test[j][0] == 0:
                dest = test[j][1]
            else:
                dest = test[j][2]
            all_items_1[dest].append(num)

counts_1.sort(reverse=True)
print("part 1:")
print(counts_1[0]*counts_1[1])


# rounds_2 = 20
# for i in range(rounds_2):
#     for j, items in enumerate(all_items_2):
#         while items:
#             num = items.pop(0)
#             counts_2[j] += 1
#             num = worry(num, ops[j])
#             #num //= 3
#             if num%test[j][0] == 0:
#                 dest = test[j][1]
#             else:
#                 dest = test[j][2]
#             all_items_2[dest].append(num)

# print(counts_2)