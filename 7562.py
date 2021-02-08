from collections import deque
from sys import stdin

k = int(stdin.readline())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, 2, -2, 2, -2, 1, -1]

result = []


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while(q):
        x, y = q.popleft()
        if x == result_x and y == result_y:
            break
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx, ny))


for _ in range(k):
    n = int(stdin.readline())
    x, y = map(int, stdin.readline().split())
    result_x, result_y = map(int, stdin.readline().split())
    graph = [[0]*n for _ in range(n)]
    bfs(x, y)
    result.append(graph[result_x][result_y])

for i in result:
    print(i)
