import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(k)

for i in distance[1:]:
    if i != INF:
        print(i)
    else:
        print("INF")
