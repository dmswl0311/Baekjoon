from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
array = []
result = []

for i in range(1, n+1):
    array.append(i)
q = deque()
start = k-1
for _ in range(n):
    if len(array) == 1:
        p = array.pop()
        q.append(p)
        break
    else:
        p = array.pop(start)
        q.append(p)
    if (start+k-1) >= len(array):
        start = start+k-1
        while(start >= len(array)):
            start = start-len(array)
    else:
        start = start+k-1

print("<", end='')
for i in range(len(q)):
    if i == len(q)-1:
        print(q[i], end='')
    else:
        print(q[i], end=', ')
print(">", end='')
