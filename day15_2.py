with open("inputs/15.txt", "r") as File:
    lines = File.readlines()


def man_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x2 - x1
    dy = y2 - y1
    return abs(dx) + abs(dy)

def merge_ranges(ranges):
    ranges.sort()
    out = []
    i = 0
    while i < len(ranges) - 1:
        r1 = ranges[i]
        r2 = ranges[i+1]
        if r2[0] > r1[1] + 1:
            i += 1
            continue
        else: 
            ranges.pop(i+1)
        if r2[1] > r1[1]:
            ranges[i] = [r1[0], r2[1]]
    return(ranges)


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


low = 0
high = 4000000
no_beacons = set()
for row in range(low, high+1):
    ranges = []
    for i, (sensor, beacon) in enumerate(zip(sensors, beacons)):
        max_dist = man_dist(sensor, beacon)
        dy = abs(row - sensor[1])
        max_dx = max_dist-dy
        x1, x2 = sensor[0] - max_dx, sensor[0] + max_dx
        x1 = max(x1, low)
        x2 = min(x2, high)
        if x2 >= x1:
            ranges.append([x1, x2])
    ranges = merge_ranges(ranges)
    if len(ranges) > 1:
        print(row, ranges)
        print ((ranges[0][1] + 1) * 4000000 + row)

