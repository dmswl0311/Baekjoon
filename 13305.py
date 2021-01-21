from sys import stdin

n = int(stdin.readline())
len = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))

result = 0
minp = price[0]

for i in range(1, n):
    if minp > price[i]:
        result += (minp*len[i-1])
        minp = price[i]
    else:
        result += (minp*len[i-1])
        minp = minp

print(result)
