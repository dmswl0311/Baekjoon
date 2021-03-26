import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
dp = [0 for i in range(n+1)]

for i in range(n):
    time, pa = map(int, input().split())
    t.append(time)
    p.append(pa)

for i in range(n-1, -1, -1):
    if t[i]+i <= n:
        dp[i] = max(p[i]+dp[i+t[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
