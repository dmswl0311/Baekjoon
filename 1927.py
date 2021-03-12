import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
result = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(h, x)
    elif x == 0:
        if len(h) > 0:
            p = heapq.heappop(h)
            result.append(p)
        else:
            result.append(0)

for i in result:
    print(i)
