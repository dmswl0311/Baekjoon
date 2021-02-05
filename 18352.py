from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
data = [-1]*(n+1)

for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

data[x] = 0
q = deque([x])

while(q):
    now = q.popleft()
    for i in graph[now]:
        if data[i] == -1:
            data[i] = data[now]+1
            q.append(i)

flag = 0

for i in range(1, n+1):
    if data[i] == k:
        print(i)
        flag = 1
if flag == 0:
    print(-1)
