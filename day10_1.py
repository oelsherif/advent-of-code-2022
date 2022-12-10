f = open("inputs/10.txt", "r")
lines = f.readlines()
f.close()

def check(count, X):
    if count%40 == 20:
        return count*X
    else:
        return 0

X = 1
count = 1
ans1 = 0
for line in lines:
    words = line.split()
    ans1 += check(count, X)
    if words[0] == 'noop':
        V = 0
        count += 1
    elif words[0] == 'addx':
        V = int(words[1])
        count += 1
        ans1 += check(count, X)
        count += 1
        X += V

print(count)
print(ans1)