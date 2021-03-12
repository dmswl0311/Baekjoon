# 다익스트라

import sys
import heapq

input = sys.stdin.readline
INF = int(1e8)

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
result = 0
result2 = 0

for _ in range(e):
    a, b, c, = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(1)

result = distance[v1]
distance = [INF]*(n+1)
dijkstra(v1)

result += distance[v2]
distance = [INF]*(n+1)
dijkstra(v2)

ql = max(distance)
for i in range(1, len(distance)):
    if i != v1 and i != v2:
        ql = min(ql, distance[i])


distance = [INF]*(n+1)
dijkstra(1)

result2 = distance[v2]
distance = [INF]*(n+1)
dijkstra(v2)

result2 += distance[v1]
distance = [INF]*(n+1)
dijkstra(v1)

ql2 = max(distance)
for i in range(1, len(distance)):
    if i != v1 and i != v2:
        ql2 = min(ql2, distance[i])

if min(ql+result, ql2+result2) >= INF:
    print(-1)
else:
    print(min(ql+result, ql2+result2))
