# DFS
# 2667번,음료수 얼려 먹기 문제와 유사

t = int(input())
result = []


def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1

    result.append(cnt)

for p in result:
    print(p)
