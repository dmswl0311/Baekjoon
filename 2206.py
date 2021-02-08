from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    cnt = 0
    flag = 0
    minus = 0
    q = deque()
    q.append((x, y))

    while(q):
        a = 0
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]+1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1 and flag == 0:
                    graph[nx][ny] = graph[x][y]+1
                    cnt += 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1 and flag == 1:
                    minus += 1
                else:
                    continue
                a += 1
        if cnt > 0:
            flag = 1
        if a == minus:
            return print(-1)
    return print(graph[n-1][m-1]+1)


print(graph)
bfs(0, 0)
