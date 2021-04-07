import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
dist = [[0]*m for _ in range(n)]

for _ in range(n):
    num_list = list(map(int, input().split()))
    graph.append(num_list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0


def bfs(q):
    while(q):
        x, y = q.popleft()
        for c in range(4):
            nx = x+dx[c]
            ny = y+dy[c]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx, ny))


cnt = 0

for i in range(n):
    cnt += sum(graph[i])

if cnt == (m*n):  # 모든 토마토가 익어있으면
    print(0)
else:
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))
            else:
                dist[i][j] = -1
    bfs(q)
    flag = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                flag = -1
                break
    if flag == -1:
        print(-1)
    else:
        max_day = 0
        for i in range(n):
            for j in range(m):
                max_day = max(max_day, dist[i][j])
        print(max_day)
