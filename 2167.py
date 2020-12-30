# 파이썬은 느리기 때문에 순차적으로 풀면 시간초과
# 부분합(DP)을 이용해야 한다고 함

import sys

n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        dp[n][m] = dp[0][0]+

k = int(sys.stdin.readline())
sum = [0]*k

for k1 in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    for a in range = (i-1, x):
        for b in range(j-1, y):
            sum[k1] += array[a][b]

for i in sum:
    print(i)
