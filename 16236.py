from collections import deque
import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상,하,좌,우
dy = [0, 0, -1, 1]

"""
now_x, now_y = 상어의 위치 저장
"""

shark = 2
cnt = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            now_x = x
            now_y = y
            # 상어의 위치 입력받았으므로 0으로 갱신해줌
            graph[x][y] = 0

while(True):
    ret, a, b, g = bfs(n, now_x, now_y, graph)
    if ret == 0:
        print(ret)
        break
    cnt += 1
    if cnt == shark:
        shark += 1
        cnt = 0
    ret += ret
    now_x = a
    now_y = b


def findTopLeft(q, n):
    tmp = []
    for x, y in q:
        tmp.append(x*n+y)
    tmp.sort()
    X = tmp[0]//n
    Y = tmp[0] % n
    return X, Y


def bfs(n, now_x, now_y, graph):
    # 값을 빼는 q
    q = deque()
    q.append((now_x, now_y))
    visited = [[0]*n for _ in range(n)]
    visited[now_x][now_y] = 1
    for length in range(1, n*n):
        # 값을 넣는 q
        nextq = deque()
        eatq = deque()
        for now_x, now_y in q:
            for i in range(4):
                nx = now_x+dx[i]
                ny = now_y+dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                # 방문 가능한지 여부
                if visited[nx][ny] == 1:
                    continue
                if shark < graph[nx][ny]:
                    continue
                nextq.append((nx, ny))
                visited[nx][ny] = 1
                if shark > graph[nx][ny] and graph[nx][ny] != 0:
                    eatq.append((nx, ny))
        if len(eatq) != 0:
            x, y = findTopLeft(eatq, n)
            return length
        if len(nextq) == 0:
            return 0, 0, 0, 0
        q = copy.deepcopy(nextq)
    return n, x, y, graph
