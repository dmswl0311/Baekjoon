# 다익스트라
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append((y, 1))
    graph[y].append((x, 1))


def dijkstra(start):
    h = []

    heapq.heappush(h, (0, start))
    distance[start] = 0

    while(h):
        x, y = heapq.heappop(h)
        if distance[y] < x:
            continue
        for i in graph[y]:
            cost = x+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(a)

if distance[b] == INF:
    print(-1)
else:
    print(distance[b])
