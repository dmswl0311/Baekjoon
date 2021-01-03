n = int(input())
array = [[0]*n for _ in range(n)]
row = (n//2)-1
col = (n//2)
flag = -1
num = 1
limit = 1

for count in range(n):
    limit += 1
    for _ in range(limit):
        row += flag
        array[row][col] = num
        num += 1
    limit -= 1
    flag *= -1
    for _ in range(limit):
        col += flag
        array[row][col] = num
        num += 1


print(array)
