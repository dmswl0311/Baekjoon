import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

b = []

for i in range(1, n+1):
    for j in range(1, n+1):
        b.append(i*j)

b.sort()
print(b[k])
