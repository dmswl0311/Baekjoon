import sys
sys.setrecursionlimit(10000)  # 최대 재귀한도 깊이 설정
input = sys.stdin.readline

t = int(input())
dx = [-1, 1, 0, 0]  # 상,하,좌,우
dy = [0, 0, -1, 1]

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0]*(m) for _ in range(n)]
    for _ in range(k):
        v1, v2 = map(int, input().split())
        graph[v2][v1] = 1

    def dfs(graph, x, y):
        if graph[x][y] == 1:
            graph[x][y] = 0
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    dfs(graph, nx, ny)
                else:
                    continue
        else:
            return False
        return True

    for i in range(n):
        for j in range(m):
            if dfs(graph, i, j) == True:
                cnt += 1
    print(cnt)
