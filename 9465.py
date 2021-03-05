t = int(input())

for i in range(t):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    d = [[0]*n for _ in range(2)]
    sum = 0

    for j in range(2):
        for k in range(n):
            x = j
            y = k
            now_x = j
            now_y = k
            if d[now_x][now_y] == 0:
                d[now_x][now_y] = 1
                for l in range(4):
                    next_x = now_x+dx[l]
                    next_y = now_y+dy[l]
                    if next_x >= 0 and next_x < 2 and next_y >= 0 and next_y < n:
                        if d[next_x][next_y] == 0:
                            if array[next_x][next_y] > array[x][y]:
                                x = next_x
                                y = next_y
                d[x][y] = 1
                for a in range(4):
                    next_x = x+dx[a]
                    next_y = y+dy[a]
                    if next_x >= 0 and next_x < 2 and next_y >= 0 and next_y < n:
                        d[next_x][next_y] = 1
                sum += array[x][y]
                print(array[x][y])

    print(sum)
