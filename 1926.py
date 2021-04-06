import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[False]*(m) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def bfs(x, y):
    area = 0
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while(q):
        x, y = q.popleft()
        area += 1
        for a in range(4):
            nx = x+dx[a]
            ny = y+dy[a]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return area


max_area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            max_area = max(bfs(i, j), max_area)
            cnt += 1
print(cnt)
print(max_area)
