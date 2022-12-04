f = open("inputs/1.txt", "r")
lines = f.readlines()
f.close()

# #part_a
# current = 0
# max = 0
# for line in lines:
#     if line == "\n":
#         if current > max:
#             max = current
#         current = 0
#     else:
#         current += int(line)
# print(max)

current = 0
calories = []
for line in lines:
    if line == "\n":
        calories.append(current)
        current = 0
    else:
        current += int(line)
calories.sort()
print("part 1:")
print(calories[-1])
print("part 2:")
print(sum(calories[-3:]))
