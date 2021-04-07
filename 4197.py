import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(map(str, input().rstrip())))

dist1 = [[0]*c for _ in range(r)]
dist2 = [[0]*c for _ in range(r)]

q = deque()
q2 = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            dist2[i][j] = 1
            q2.append((i, j))
        if graph[i][j] == 'F':
            dist1[i][j] = 1
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while(q):
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c:
            if graph[nx][ny] != '#' and dist1[nx][ny] == 0:
                dist1[nx][ny] = dist1[x][y]+1
                q.append((nx, ny))


def bfs(q2):
    while(q2):
        x, y = q2.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < r and ny < c:
                if graph[nx][ny] != '#' and dist2[nx][ny] == 0:
                    if dist1[nx][ny] <= dist2[x][y]+1:
                        dist2[nx][ny] = -1
                    else:
                        dist2[nx][ny] = dist2[x][y]+1
                        q2.append((nx, ny))
            else:
                return print(dist2[x][y])
    print("IMPOSSIBLE")


bfs(q2)
