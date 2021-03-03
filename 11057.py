# DP

n = int(input())
d = [[0]*10 for _ in range(n+1)]
d[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n+1):
    for j in range(0, 10):
        if j == 0:
            d[i][j] = sum(d[i-1]) % 10007
        else:
            d[i][j] = (d[i][j-1]-d[i-1][j-1]) % 10007

print(sum(d[n-1]) % 10007)
