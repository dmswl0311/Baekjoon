from sys import stdin

n = int(stdin.readline())
len = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))

result = 0
start = 0

while(start < n-1):
    for j in range(start+1, n):
        if (price[start] < price[j]):
            result += (price[start]*len[j-1])
        else:
            result += (price[start]*len[j-1])
            start = j

print(result)
