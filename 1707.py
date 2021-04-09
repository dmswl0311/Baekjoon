import sys
from collections import deque
input = sys.stdin.readline

k = int(input())


def bfs(v):
    q = deque([v])
    visited[v] = True
    while(q):
        x = q.popleft()
        check_list[x] += 1
        for target in graph[x]:
            if not visited[target]:
                visited[target] = True
                q.append(target)


for _ in range(k):

    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    check_list = [0]*(v+1)
    visited = [False]*(v+1)

    for _ in range(e):
        num, v2 = map(int, input().split())
        graph[num].append(v2)

    for i in range(1, v+1):
        if not visited[i]:
            bfs(i)
    print(check_list)
    flag = 1
    for i in check_list[1:]:
        if i > 1:
            flag = 0
            break

    if flag == 0:
        print("NO")
    else:
        print("YES")
