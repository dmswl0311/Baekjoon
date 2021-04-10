import sys
from collections import deque
input = sys.stdin.readline

k = int(input())


def bfs(v):
    q = deque([v])
    visited[v] = True
    check_list[v] = 1
    while(q):
        x = q.popleft()
        for target in graph[x]:
            if not visited[target]:
                visited[target] = True
                check_list[target] = 3-check_list[x]
                q.append(target)
            else:
                if check_list[target] == check_list[x]:
                    return False
    return True


for _ in range(k):

    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    check_list = [0]*(v+1)
    visited = [False]*(v+1)
    flag = True

    for _ in range(e):
        num, v2 = map(int, input().split())
        graph[num].append(v2)
        graph[v2].append(num)

    for i in range(1, v+1):
        if not visited[i]:
            if not bfs(i):
                flag = False
                break
    if flag == False:
        print("NO")
    else:
        print("YES")
