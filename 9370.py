import sys
input = sys.stdin.readline
INF = int(1e9)

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 교차로, 도로, 목적지 후보의 개수
    n, m, t = map(int, input().split())
    # 예술가 출발지, 문제 설명 g,h 교차로
    s, g, h = map(int, input().split())

    # 출발지 후보 저장
    result = []

    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0

    for _ in range(m):
        a, b, d = map(int, input().split())
        # 양방향 도로
        graph[a][b] = d
        graph[b][a] = d

    for i in range(t):
        x = int(input())
        result.append(x)

    result.sort()

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    print(graph)
    for end in result:
        if ((graph[s][g] != INF) and (graph[g][h] != INF) and (graph[h][end] != INF)):
            print(end, end=" ")
    print("")
