# 출력형식 오류-> 마지막 배열 출력하는 for문에서 print(' ') 말고 print()쓰기

n = int(input())
k = int(input())
array = [[0]*n for _ in range(n)]

row = -1
col = 0
flag = 1
limit = n
num = n*n
result_row = 0
result_col = 0

while(limit != 0):
    for _ in range(limit):
        row += flag
        array[row][col] = num
        if num == k:
            result_row = row
            result_col = col
        num -= 1
    limit -= 1
    for _ in range(limit):
        col += flag
        array[row][col] = num
        if num == k:
            result_row = row
            result_col = col
        num -= 1
    flag *= -1

for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print()

print(result_row+1, result_col+1)
