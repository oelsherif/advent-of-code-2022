with open("inputs/test21.txt", "r") as File:
    lines = [line.split() for line in File]

def operate(a, symbol, b):
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '*':
        return a * b
    elif symbol == '/':
        return a // b

def value(s):
    arr = d[s]
    if len(arr) == 1:
        return int(arr[0])
    a = value(arr[0])
    sym = arr[1]
    b = value(arr[2])
    return operate(a, sym, b)

d = {}
for line in lines:
    d[line[0][:-1]] = line[1:]

print(value('root'))