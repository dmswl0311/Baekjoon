# BFS
# 미로 찾기

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    q = deque()
    q.append((x, y))
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx, ny))
            else:
                continue


dfs(0, 0)
print(graph[n-1][m-1])
