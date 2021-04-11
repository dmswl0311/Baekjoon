import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 동전 가치
value = []
for _ in range(n):
    value.append(int(input()))

# 동전 가치 중복 제거 / sorted 왜하는거지?
value = sorted(list(set(value)))

# dp
dp = [10001]*(k+1)
dp[0] = 0

for i in range(1, k+1):
    for c in value:
        if i-c < 0:
            break
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
