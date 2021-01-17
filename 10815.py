import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()
result = [0]*(max(b)+1)

for i in range(m):
    for j in range(n):
        if(b[i] == a[j]):
            result[i] = 1
            break
        elif(b[i] > a[j]):
            continue
        else:
            result[i] = 0
            break

for i in result:
    print(i, end=' ')
