f = open("inputs/10.txt", "r")
lines = f.readlines()
f.close()

def action(pos, X):
    global msg
    if pos in range(X-1, X+2):
        msg += "#"
    else:
        #msg += "."
        msg += " "
    pos = (pos+1)%40
    return pos

msg = ""
X = 1
pos = 0

for line in lines:
    words = line.split()
    if words[0] == 'noop':
        pos = action(pos, X)
    elif words[0] == 'addx':
        V = int(words[1])
        pos = action(pos, X)
        pos = action(pos, X)
        X += V

i = 0
while i in range(len(msg)):
    print(msg[i:i+40])
    i += 40
