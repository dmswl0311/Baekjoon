t = int(input())
result = []
for i in range(t):
    sum = 0
    k = int(input())
    n = int(input())
    array = [[0]*n for _ in range(k+1)]
    for j in range(n):
        array[0][j] = j+1

    for y in range(1, k+1):
        for x in range(0, n):
            sum = sum+array[y-1][x]
            array[y][x] = sum
        sum = 0
    result.append(array[k][n-1])

for i in result:
    print(i)
