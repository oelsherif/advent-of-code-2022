with open("inputs/20.txt", "r") as File:
    nums = [int(line) for line in File]

#nums = [1, 2, -3, 3, -2, 0, 4]
n = len(nums)
order = [i for i in range(n)]
count = 0
for count in range(n):
    i = order.index(count)
    num = nums[i]
    if num > 0:
        for k in range(num):
            a = (i+k)%n
            b = (i+k+1)%n
            nums[a], nums[b] = nums[b], nums[a]
            order[a], order[b] = order[b], order[a]
    elif num < 0:
        for k in range(abs(num)):
            a = (i-k)%n
            b = (i-k-1)%n
            nums[a], nums[b] = nums[b], nums[a]
            order[a], order[b] = order[b], order[a]

loc = nums.index(0)
x, y, z = (loc+1000)%n, (loc+2000)%n, (loc+3000)%n
a, b, c = nums[x], nums[y], nums[z]
print(a, b, c)
print(a + b + c)