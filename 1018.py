n, m = map(int, input().split())
array = [[0]*m for _ in range(n)]

for i in range(n):
    j = 0
    str = input()
    for s in str:
        array[i][j] = s
        j += 1
    str = ''

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()
