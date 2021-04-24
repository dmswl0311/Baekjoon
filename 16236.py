from collections import deque
import copy
INF = 1e9
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상,하,좌,우
dy = [0, 0, -1, 1]

"""
now_x, now_y = 상어의 위치 저장
"""

shark = 2
now_x = 0
now_y = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            now_x = x
            now_y = y
            # 상어의 위치 입력받았으므로 0으로 갱신해줌
            graph[x][y] = 0


def bfs(x, y):
    visited = [[-1]*n for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == -1 and shark >= graph[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx, ny))
    return visited


def l(visited):

    x, y = 0, 0
    min_fish = INF
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and shark > graph[i][j] and graph[i][j] >= 1:
                """
                먹을 수 있는 것들 중 가까운 값 찾음,
                0,0부터 찾으므로 자연스럽게 가장 위에 있는 물고기, 왼쪽에 있는 물고기로 찾아짐
                """
                if visited[i][j] < min_fish:
                    x, y = i, j
                    min_fish = visited[i][j]
    if min_fish == INF:
        return None
    else:
        return x, y, min_fish


eat = 0
result = 0

while(True):
    value = l(bfs(now_x, now_y))
    if value == None:
        print(result)
        break
    else:
        now_x = value[0]
        now_y = value[1]
        result += value[2]
        graph[now_x][now_y] = 0
        eat += 1
        if eat >= shark:
            shark += 1
            eat = 0
