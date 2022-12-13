import ast
with open("inputs/13.txt",'r') as file:
    lines = file.readlines()

def compare(left, right):
    len_left = len(left)
    len_right = len(right)
    for i in range(max(len_left, len_right)):
        if i == len_left:
            return True
        elif i == len_right:
            return False
        l = left[i]
        r = right[i]
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
        else:
            if type(l) == int:
                l = [l]
            if type(r) == int:
                r = [r]
            if compare(l, r) != None:
                return compare(l, r)
    

lefts, rights = [], []
for i in range(len(lines)):
    if i%3 == 0:
        lefts.append(ast.literal_eval(lines[i]))
        rights.append(ast.literal_eval(lines[i+1]))

score = 0
for i, (left, right) in enumerate(zip(lefts, rights)):
    if compare(left, right):
        score += (i+1)

print("part 1:")
print(score)

div1 = [[2]]
div2 = [[6]]

packets = lefts + rights + [div1, div2]
i = 0
n = len(packets)
while i < n-1: #bubble sort, could be a lot faster
    if compare(packets[i+1], packets[i]):
        packets[i], packets[i+1] = packets[i+1], packets[i]
        i = 0
        continue
    i += 1

i1 = packets.index(div1) + 1
i2 = packets.index(div2) + 1
#print(i1, i2)
print("part 2:")
print(i1*i2)