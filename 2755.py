import sys

T = int(sys.stdin.readline())
list = []
list2 = []
sum = 0

for i in range(T):
    k = int(sys.stdin.readline())
    list.append(k)
    n = int(sys.stdin.readline())
    list2.append(n)

for i in range(k):
    for j in range(1, n+1):
        sum += j

print(sum)
