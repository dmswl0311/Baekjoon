import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [0]*200000
graph[n] = 0
visited = [False]*200000
# 걷기, 순간이동은 2*현재위치
dx = ['-1', '1', '2']

q = deque()
q.append(n)
visited[n] = True
while(q):
    x = q.popleft()
    if x == k:
        print(graph[x])
        break
    for i in range(3):
        if dx[i] == '-1':
            nx = x-1
        elif dx[i] == '1':
            nx = x+1
        elif dx[i] == '2':
            nx = x*2
        if (0 > nx or nx >= 200000):
            continue
        if not visited[nx]:
            graph[nx] = graph[x]+1
            visited[nx] = True
            q.append(nx)
