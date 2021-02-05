from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = ['false']*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
cnt = 0
while(q):
    now = q.popleft()
    cnt += 1
    visited[now] = True
    for i in graph[now]:
        if visited[i] == 'false':
            q.append(i)
            visited[i] = True

print(cnt-1)
