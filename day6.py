f = open("inputs/6.txt", "r")
line = f.read()
f.close()

pck_len = 4
msg_len = 14

for i in range(len(line) - pck_len):
    word = line[i: i + pck_len]
    for j, char in enumerate(word):
        if char in word[j+1:]:
            break
    else:
        ans1 = i + pck_len
        break

for i in range(len(line) - msg_len):
    word = line[i: i + msg_len]
    for j, char in enumerate(word):
        if char in word[j+1:]:
            break
    else:
        ans2 = i + msg_len
        break

print("part 1:")
print(ans1)
print("part 2:")
print(ans2)