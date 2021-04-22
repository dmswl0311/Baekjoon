from collections import deque

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

global air_machine


def dust():
    global air_machine
    global graph_dust
    # 확산 graph 따로 지정
    graph_dust = [[0]*c for _ in range(r)]

    # 미세먼지가 있는 좌표 따로 저장 (시간 단축), 공기청정기 위치 저장
    dust = []
    air_machine = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                dust.append((i, j))
            if graph[i][j] == -1:
                air_machine.append((i, j))
                graph_dust[i][j] = -1

    for x, y in dust:
        cnt = 0
        for next in range(4):
            nx = x+dx[next]
            ny = y+dy[next]
            # 인접한 방향에 공기청정기 or 칸이 없을때
            if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny] == -1:
                continue
            graph_dust[nx][ny] += graph[x][y]//5
            cnt += 1

        graph_dust[x][y] += graph[x][y]-((graph[x][y]//5)*cnt)
        # print("x는 {0} y는 {1} cnt는 {2}".format(x, y, cnt))


def air():
    global r
    global c
    r = r-1
    c = c-1
    # 반시계방향 연산 -----------
    row = air_machine[0][0]

    temp = graph_dust[row][c]
    for i in range(c, 0, -1):
        graph_dust[row][i] = graph_dust[row][i-1]
    graph_dust[row][0] = 0

    temp_1 = graph_dust[0][c]
    for i in range(0, row-1):
        graph_dust[i][c] = graph_dust[i+1][c]
    graph_dust[row-1][c] = temp

    temp_2 = graph_dust[0][0]
    for i in range(0, c-1):
        graph_dust[0][i] = graph_dust[0][i+1]
    graph_dust[0][c-1] = temp_1

    for i in range(row, 1, -1):
        graph_dust[i][0] = graph_dust[i-1][0]
    graph_dust[1][0] = temp_2

    # 시계방향 연산 -----------
    row = air_machine[1][0]

    temp = graph_dust[row][c]
    for i in range(c, 0, -1):
        graph_dust[row][i] = graph_dust[row][i-1]
    graph_dust[row][0] = 0


for _ in range(t):
    dust()
    air()
    r = r+1
    c = c+1
    # 원래 그래프에 확산한 graph_dust 옮기기
    for i in range(r):
        for j in range(c):
            graph[i][j] = graph_dust[i][j]

cnt = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            cnt += graph[i][j]

print(graph)
print(cnt)
