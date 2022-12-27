with open("inputs/21.txt", "r") as File:
    lines = [line.split() for line in File]

def operate(a, symbol, b):
    if symbol == '+':
        return a + b
    elif symbol == '-':
        return a - b
    elif symbol == '*':
        return a * b
    elif symbol == '/':
        return a / b

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

monk1 = d['root'][0]
monk2 = d['root'][2]

exp = 15
start = 0
end = 10**(exp+1)
while True:
    flag = 0
    for test in range(start, end + 1, 10**exp):
        d['humn'] = [test]
        val1 = value(monk1)
        val2 = value(monk2)
        if val1 > val2:
            #print(f"for {test}: 1 is bigger")
            continue
        elif val2 > val1:
            #print(f"for {test}: 2 is bigger")
            end = test
            start = end - 10**exp
            exp -= 1
            break
        elif val1 == val2:
            flag = True
            print(f"The Answer is {test}")
            break
    if flag:
        break