n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0]  # 0,1,2,3 방향
dy = [0, 1, 0, -1]
for i in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0


def clean(x, y, d):
    global cnt
    # 현재 위치 청소
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1
    for _ in range(4):
        nd = (d+3) % 4
        nx = x+dx[nd]
        ny = y+dy[nd]
        # 청소 할 공간 없는 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 왼쪽 방향에 청소하지 않은 공간 존재
        if graph[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        # 없으면 회전, 2번으로 돌아가기
        d = nd
    # 후진
    nd = (d+2) % 4
    nx = x+dx[nd]
    ny = y+dy[nd]
    if graph[nx][ny] == 1:
        return
    clean(nx, ny, d)


clean(r, c, d)
print(cnt)
