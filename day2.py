f = open("inputs/2.txt", "r")
lines = f.readlines()
f.close()

values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

score1 = 0
for line in lines:
    words = line.split()
    diff = (values[words[1]] + 1 - values[words[0]]) % 3
    score1 += 3 * diff
    score1 += values[words[1]]

score2 = 0
for line in lines:
    words = line.split()
    score2 += (values[words[0]] + values[words[1]]) % 3 + 1
    score2 += (values[words[1]] - 1) * 3


print("part 1:")
print(score1)
print("part 2:")
print(score2)