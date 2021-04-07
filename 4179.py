import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

r, c = map(int, input().split())
graph = []
flag = 0
for _ in range(r):
    graph.append(list(map(str, input().rstrip())))

q = deque()
q2 = deque()

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            q2.append((i, j))
        if graph[i][j] == 'F':
            q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(q):
    global cnt
    cnt = 0
    dist1 = [[0]*c for _ in range(r)]
    visited = [[False]*c for _ in range(r)]
    for i in q:
        visited[i[0]][i[1]] = True
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < r and ny < c:
                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dist1[nx][ny] = dist1[x][y]+1
                    q.append((nx, ny))
                    cnt += 1
    return dist1


fire = bfs(q)
if cnt == 0:
    flag = 1
jihun = bfs(q2)

min_dist = INF

if flag == 0:
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0 or i == r-1 or j == c-1:
                if jihun[i][j] < fire[i][j]:
                    min_dist = min(min_dist, jihun[i][j])
    if min_dist != INF:
        print(min_dist+1)
    else:
        print("IMPOSSIBLE")
else:
    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0 or i == r-1 or j == c-1:
                if jihun[i][j] != 0:
                    min_dist = min(min_dist, jihun[i][j])
    if min_dist != INF:
        print(min_dist+1)
    else:
        print("IMPOSSIBLE")
