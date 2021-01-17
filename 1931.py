import sys

n = int(sys.stdin.readline())
a = [0]*n
array = [0]*n

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    a[i] = (start, end)

a.sort(key=lambda x: (x[0], x[1]))
result = 1
i = 0

while(i < n):
    start = i
    for j in range(start+1, n):
        if (a[start][0] <= a[j][0] and a[start][1] <= a[j][0]):
            result += 1
            start = j
        else:
            continue
    array[i] = result
    i += 1
    result = 1

print(max(array))
