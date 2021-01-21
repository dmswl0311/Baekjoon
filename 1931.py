from sys import stdin

n = int(stdin.readline())
array = [0]*n
result = []
for i in range(n):
    start, end = map(int, stdin.readline().split())
    array[i] = (start, end)

array.sort(key=lambda x: (x[0], x[1]))
for i in range(n):
    cnt = 1
    next = i
    for j in range(i+1, n):
        if (array[next][1] <= array[j][0]):
            next = j
            cnt += 1
    result.append(cnt)

print(max(result))
