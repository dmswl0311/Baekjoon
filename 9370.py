import sys
import heapq

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

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        # 양방향 도로
        graph[a].append((b, d))
        graph[b].append((a, d))

    for i in range(t):
        x = int(input())
        result.append(x)

    result.sort()

    def dijkstra(start):
        distance = [INF]*(n+1)
        h = []
        heapq.heappush(h, (0, start))
        distance[start] = 0

        while(h):
            dist, now = heapq.heappop(h)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = i[1]+dist
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappushpop(h, (cost, i[0]))
        return distance

    start = dijkstra(s)
    g_g = dijkstra(g)
    h_g = dijkstra(h)

    for e in result:
        if ((start[g]+g_g[h]+h_g[e] <= start[e]) or (start[h]+h_g[g]+g_g[e] <= start[e])):
            print(e, end=" ")
    print("")
