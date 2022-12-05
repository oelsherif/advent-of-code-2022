f = open("inputs/4.txt", "r")
lines = f.readlines()
f.close()

count1 = 0
count2 = 0
for line in lines:
    ranges = line[:-1].replace(',', '-').split('-')
    start1, end1, start2, end2 = [int(i) for i in ranges]
    if (start1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2):
        print (start1, end1, start2, end2)
        count1 += 1
    if (start2 >= start1 and start2 <= end1) or (start1 >= start2 and start1 <= end2):
        count2 += 1

print("part 1:")
print(count1)
print("part 2:")
print(count2)

