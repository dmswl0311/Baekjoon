import sys

n, k = map(int, sys.stdin.readline().split())
array = [0]*n
result = [0]*n
for i in range(n):
    area, g, s, c = map(int, sys.stdin.readline().split())
    array[i] = (area, g, s, c)

array.sort(key=lambda x: (-x[1], -x[2], -x[3]))

start = 0
cnt = 1
for i in range(n):
    start = i
    for j in range(start, n):
        if (array[j][1] == array[j+1][1] and array[j][2] == array[j+1][2] and array[j][3] == array[j+1][3]):
            result[j] = cnt
            result[j+1] = cnt
            start = j
        else:
            result[j] = cnt
            cnt += 1
            break

print(result)
