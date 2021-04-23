n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 바람의 방향에 따른 모래 비율
left = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [
    5, 'a', 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
down = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [
    2, 7, 0, 7, 2], [0, 10, 'a', 10, 0], [0, 0, 5, 0, 0]]
right = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [
    0, 0, 0, 'a', 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
up = [[0, 0, 5, 0, 0], [0, 10, 'a', 10, 0], [
    2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

# 달팽이 방향으로 움직이기
row = n//2
column = n//2
flag = -1
cnt = 0

while(row != 0 and column != 0):
    cnt += 1
    for _ in range(cnt):
        graph[row][column+flag] = -1
        column = column+flag
    flag *= -1
    for _ in range(cnt):
        graph[row+flag][column] = -1
        row = row+flag
    cnt += 1
    for _ in range(cnt):
        graph[row][column+flag] = -1
        column = column+flag
    flag *= -1
    for _ in range(cnt):
        graph[row+flag][column] = -1
        row = row+flag

print(graph)
