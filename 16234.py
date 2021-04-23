from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, index):
    count = 1
    q = deque()
    q.append((x, y))
    # 연결되어 있는 나라 저장
    location = []
    union[x][y] = index
    location.append((x, y))
    hap = graph[x][y]

    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or union[nx][ny] != -1:
                continue
            if l <= abs(graph[x][y]-graph[nx][ny]) <= r:
                count += 1
                hap += graph[nx][ny]
                q.append((nx, ny))
                location.append((nx, ny))
                union[nx][ny] = index
    for i, j in location:
        graph[i][j] = hap//count
    return count


total_count = 0

while(True):
    union = [[-1]*n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1

    """
    index가 같은걸로 묶이는 그룹의 개수인데 
    그룹의 개수가 n*n이라는 것은 모든 원소들이
    각각 따로 묶였다는 것! => 인구이동 x
    """

    if index == n*n:
        break
    total_count += 1

print(total_count)
