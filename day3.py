f = open("inputs/3.txt", "r")
lines = f.readlines()
f.close()

def value(char):
    if char.islower():
        return ord(char) - ord('a') + 1
    elif char.isupper():
        return ord(char) - ord('A') + 27
    else:
        return -1

sum1 = 0
for line in lines:
    n = len(line) - 1
    for char in line[:n//2]:
        if char in line[n//2:]:
            sum1 += value(char)
            break

sum2 = 0
for i in range(0, len(lines), 3):
    trio = lines[i:i+3]
    for char in trio[0]:
        if char in trio[1] and char in trio[2]:
            sum2 += value(char)
            break

print("part 1:")
print(sum1)
print("part 2:")
print(sum2)