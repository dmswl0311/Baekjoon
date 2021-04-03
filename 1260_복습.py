import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = ['false']*(n+1)
visited_b = ['false']*(n+1)
data = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
    data.append(i)


def dfs(data, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in data[v]:
        if visited[i] == 'false':
            dfs(data, i, visited)


q = deque([v])
visited_b[v] = True
cnt = 0


def bfs(data, visited_b):
    global cnt
    while(q):
        now = q.popleft()
        cnt += 1
        if cnt > n:
            break
        print(now, end=' ')
        for i in data[now]:
            if visited_b[i] == 'false':
                q.append(i)
                visited_b[i] = True


dfs(data, v, visited)
print()
bfs(data, visited_b)
