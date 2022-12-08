f = open("inputs/8.txt", "r")
lines = f.readlines()
f.close()

mat = []
for line in lines:
    row = [int(char) for char in line[:-1]]
    mat.append(row)

m, n = len(mat), len(mat[0])

ans1 = 2*(m+n)-4
for j in range(1, n-1):
    col = [mat[l][j] for l in range(m)]
    for i in range(1, m-1):
        num = mat[i][j]
        if num > max(mat[i][:j]) or num > max(mat[i][j+1:]) or num > max(col[:i]) or num > max(col[i+1:]):
            ans1 += 1

ans2 = 0 
for j in range(1, n-1):
    col = [mat[l][j] for l in range(m)]
    for i in range(1, m-1):
        num = mat[i][j]
        up, down, left, right = i, m-i-1 , j, n-j-1 
        for k in range(i-1, -1, -1):
            if col[k] >= num:
                up = i-k
                break
        for k in range(i+1, m):
            if col[k] >= num:
                down = k-i
                break
        for k in range(j-1, -1, -1):
            if mat[i][k] >= num:
                left = j-k
                break
        for k in range(j+1, n):
            if mat[i][k] >= num:
                right = k-j
                break
        score = up*down*left*right
        if score > ans2:
            ans2 = score

print("part 1:")
print(ans1)
print("part 2:")
print(ans2)

