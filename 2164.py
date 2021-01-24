from collections import deque
from sys import stdin

q = deque()
n = int(stdin.readline())

for i in range(1, n+1):
    q.append(i)

while(len(q) != 1):
    q.popleft()
    p = q.popleft()
    q.append(p)

print(q[0])
