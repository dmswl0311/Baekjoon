# 다익스트라

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

result = 0
result2 = 0

for _ in range(e):
    a, b, c, = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF]*(n+1)
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)

        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
    return distance


one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)

cnt = min(one[v1]+v1_[v2]+v2_[n], one[v2]+v2_[v1]+v1_[n])

if cnt >= INF:
    print(-1)
else:
    print(cnt)
