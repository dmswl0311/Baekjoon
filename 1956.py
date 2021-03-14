import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

graph = [[INF]*(v+1) for _ in range(v+1)]

for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            graph[i][j] = 0

for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, v+1):
    for j in range(1, v+1):
        if graph[i][j] != INF:
            print(graph[i][j], end=" ")
        else:
            print("INFINITY", end=" ")
    print(" ")
