# 다익스트라
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().split())
graph = [[] for _ in range(d+1)]
distance = [INF]*(d+1)

for i in range(n):
    x, y, l = map(int, input().split())
    graph[x].append((y, l))

print(graph)


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


dijkstra(0)
sum = 0

print(distance)

for i in distance:
    if i != INF:
        sum += i

print(sum)
