import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*n]*n
result_graph = [[1]*n for _ in range(n)]
result = 0

for i in range(n):
    num_list = list(map(int, input().split()))
    graph[i] = num_list

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or k == i:
                continue
            if graph[i][k]+graph[k][j] == graph[i][j]:
                result_graph[i][j] = 0
                # 구해진 최단 거리와 거쳐가서 구해진 거리가 같다면, 바로 가는 길은 없다는 뜻이므로
            elif graph[i][k]+graph[k][j] < graph[i][j]:
                result = -1
                # 최단 경로가 더 크면 잘못되었다는 의미이므로 -1

if result != -1:
    for i in range(n):
        for j in range(i, n):
            # j가 i부타 시작하는 이유는 0부터 시작하면 result_graph의 모든 값을 저장하기 때문,
            # i부터 시작하면 대각선 위로 값들만 저장함
            if result_graph[i][j]:
                result += graph[i][j]
print(result)
