with open("inputs/25.txt", "r") as File:
    lines = [line[:-1] for line in File]

def SNAFU_TO_DEC(s):
    rev = s[::-1]
    num = 0
    for i, char in enumerate(rev):
        val = digits[char]
        num += val * 5**i
    return num

def DEC_TO_SNAFU(num):
    s = ""
    while num:
        dig = num % 5
        if dig == 0:
            s = '0' + s
        elif dig == 1:
            s = '1' + s
            num -= 1
        elif dig == 2:
            s = '2' + s
            num -= 2
        elif dig == 3:
            s = '=' + s
            num += 2
        elif dig == 4:
            s = '-' + s
            num += 1
        num //= 5
    return s

digits = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

nums = [SNAFU_TO_DEC(s) for s in lines]
add = sum(nums)
ans = DEC_TO_SNAFU(add)
print(ans)