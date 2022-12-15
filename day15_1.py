with open("inputs/15.txt", "r") as File:
    lines = File.readlines()


def man_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1
    return abs(dx) + abs(dy)

sensors = []
beacons = []
for line in lines:
    line = line.split()
    arr = [line[2], line[3], line[8], line[9]]
    for i, word in enumerate(arr):
        word = word.replace('x', '').replace('y', '')
        word = word.replace(',','').replace('=','').replace(':','')
        arr[i] = int(word)
    sensors.append(arr[0:2])
    beacons.append(arr[2:4])


example_row = 10
actual_row = 2000000
row = actual_row

no_beacons = set()
for i, (sensor, beacon) in enumerate(zip(sensors, beacons)):
    max_dist = man_dist(sensor, beacon)
    dy = abs(row - sensor[1])
    max_dx = max_dist-dy
    x1, x2 = sensor[0] - max_dx, sensor[0] + max_dx
    for x in range(x1, x2+1):
        pos = [x, row]
        if (pos not in beacons):
            no_beacons.add(x)
print(len(no_beacons))
