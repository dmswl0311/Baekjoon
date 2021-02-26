from sys import stdin

n = int(stdin.readline())
len = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
sum = 0
min = cost[0]

for i in range(1, n):
    if min > cost[i]:
        sum += min*len[i-1]
        min = cost[i]
    else:
        sum += min*len[i-1]
        min = min

print(sum)
