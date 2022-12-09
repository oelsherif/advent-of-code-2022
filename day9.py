f = open("inputs/9.txt", "r")
lines = f.readlines()
f.close()

direction = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0]
}

def new_tail(head, tail):
    del_x = head[0] - tail[0]
    del_y = head[1] - tail[1]
    if abs(del_x) + abs(del_y) < 3:
        if abs(del_x) == 2:
            tail[0] += del_x//2
        elif abs(del_y) == 2:
            tail[1] += del_y//2
    
    elif abs(del_x) + abs(del_y) == 3:
        if abs(del_x) == 1:
            tail[0] += del_x
            tail[1] += del_y//2
        elif abs(del_y) == 1:
            tail[0] += del_x//2
            tail[1] += del_y
    else:
        tail[0] += del_x//2
        tail[1] += del_y//2
    return (tail)


#part1
# head = [0,0]
# tail = [0,0]
# tails = []
# count1 = 0
# for line in lines:
#     words = line.split()
#     letter = words[0]
#     num = int(words[1])
#     for i in range(num):
#         dir = direction[letter]
#         head[0] += dir[0]
#         head[1] += dir[1]
#         tail = new_tail(head, tail)
#         if tail not in tails:
#             tails.append(tail[:])
#             count1 += 1
# print("part 1:")
# print(count1)

num_nodes = 10
nodes = [ [0,0] for i in range(num_nodes)]
node1s = []
node9s = []
count1, count2 = 0, 0

for line in lines:
    words = line.split()
    letter = words[0]
    num = int(words[1])
    for i in range(num):
        dir = direction[letter]
        nodes[0][0] += dir[0]
        nodes[0][1] += dir[1]
        for i in range(1, num_nodes):
            nodes[i] = new_tail(nodes[i-1], nodes[i])

        if nodes[1] not in node1s:
            node1s.append(nodes[1][:])
            count1 += 1
        if nodes[9] not in node9s:
            node9s.append(nodes[9][:])
            count2 += 1

print("part 1:")
print(count1)
print("part 2:")
print(count2)
