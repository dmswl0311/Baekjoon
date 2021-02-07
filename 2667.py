from sys import stdin

n = int(stdin.readline())
graph = [[0]*n for _ in range(n)]

for i in range(n):
    num_list = list(str(stdin.readline()))
    for j in range(n):
        graph[i][j] = int(num_list[j])
    num_list = ''

total_cnt = 0
cnt = 0
result_2 = []


def dfs(x, y):
    global cnt
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False


for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j) == True:
            total_cnt += 1
            result_2.append(cnt)

print(total_cnt)

result_2.sort()
for i in result_2:
    print(i)
