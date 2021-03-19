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
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

comp = INF

for i in range(1, v+1):
    for j in range(1, v+1):
        if i != j:
            if graph[i][j] != INF and graph[j][i] != INF:
                comp = min(comp, graph[i][j]+graph[j][i])
            else:
                continue

if comp == INF:
    print(-1)
else:
    print(comp)
