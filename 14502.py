from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
g = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hubo = []
virus = []
q = deque()


def bfs(x, y):  # bfs 함수
    q.append((x, y))
    visited[x][y] = True
    while (q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and g[nx][ny] == 0:
                visited[nx][ny] = True
                g[nx][ny] = 2
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            hubo.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

c = list(combinations(hubo, 3))

result = []

for a in c:
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            g[i][j] = graph[i][j]
    for b in range(3):
        g[a[b][0]][a[b][1]] = 1
    for s in virus:
        if not visited[s[0]][s[1]]:
            bfs(s[0], s[1])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                cnt += 1
    result.append(cnt)

print(max(result))
