from sys import stdin

n = int(stdin.readline())
array = []

for i in range(n):
    start, end = map(int, stdin.readline().split())
    array.append((start, end))

array.sort(key=lambda x: (x[1], x[0]))
last = 0
cnt = 0

for i, j in array:
    if i >= last:
        cnt += 1
        last = j

print(cnt)
