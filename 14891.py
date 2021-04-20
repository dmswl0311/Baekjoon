graph = [list(map(int, input())) for _ in range(4)]
k = int(input())

for i in range(k):
    n, d = map(int, input().split())
    move = [0]*4  # graph 회전 저장하는 리스트
    n = n-1  # 배열 0부터 시작하니까 n에서 1 빼줌
    move[n] = d

    # left와 right 톱니바퀴 비교
    # left의 2번째(원래는 3번째)와 right의 6번째는 항상 맞닿아있음
    for left in range(n-1, -1, -1):
        right = left+1
        if graph[left][2] == graph[right][6]:
            break
        else:
            move[left] = move[right]*(-1)
    for right in range(n+1, 4, 1):
        left = right-1
        if graph[left][2] == graph[right][6]:
            break
        else:
            move[right] = move[left]*(-1)

    # 비트연산
    for m in range(4):
        if move[m] == -1:  # 반시계
            a = [graph[m][0]]
            b = graph[m][1:]
            graph[m] = b+a
        elif move[m] == 1:  # 시계
            a = graph[m][:7]
            b = [graph[m][-1]]
            graph[m] = b+a

result = 0

for m in range(4):

    if graph[m][0] == 0:
        continue
    else:
        if m == 0:
            result += 1
        elif m == 1:
            result += 2
        elif m == 2:
            result += 4
        elif m == 3:
            result += 8

print(result)
