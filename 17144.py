from collections import deque

r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
visited = [[False]*c for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 확산 graph 따로 지정
graph_dust = [[0]*c for _ in range(r)]

# 미세먼지가 있는 좌표 따로 저장
dust = []
for i in range(r):
    for j in range(c):
        if graph[i][j] != 0 and graph[i][j] != -1:
            dust.append((i, j))
        if graph[i][j] == -1:
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
    print("x는 {0} y는 {1} cnt는 {2}".format(x, y, cnt))

print(graph_dust)
