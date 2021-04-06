import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dist = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    dist[x][y] = 1
    while(q):
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1:
                    # 방문처리
                    graph[nx][ny] = 0
                    # 거리 값 갱신, 현재 값보다 1만큼 떨어져 있으므로
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx, ny))


bfs(0, 0)
print(dist[n-1][m-1])
