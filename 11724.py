# 점의 개수도 연결 간선 개수에 포함됨

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while (q):
        x = q.popleft()
        for target in graph[x]:
            if not visited[target]:
                visited[target] = True
                q.append(target)
            else:
                continue


cnt = 0
for i in range(1, n+1):
    if not visited[i] and len(graph[i]) != 0:
        bfs(i)
        cnt += 1
for i in range(1, n+1):
    if not visited[i] and len(graph[i]) == 0:
        cnt += 1

print(cnt)
