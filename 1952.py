m, n = map(int, input().split())
array = [[0]*n for _ in range(m)]

result = 0

row = 0
col = -1
flag = 1
mlimit = m
nlimit = n

while(nlimit != 0 and mlimit != 0):
    for _ in range(nlimit):
        col += flag
        array[row][col] = 1
    flag *= -1
    mlimit -= 1
    if (array[row+flag][col] != 1):
        result += 1
    for _ in range(mlimit):
        row += flag
        array[row][col] = 1
    nlimit -= 1
    if (array[row][col+flag] != 1):
        result += 1

print(result)
