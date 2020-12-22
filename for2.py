import sys
n = int(sys.stdin.readline())
list = []
sum = 0

for i in range(0, n):
    A, B = map(int, sys.stdin.readline().split())
    sum = A+B
    list.append(sum)

for i in range(1, n+1):
    print("Case #%i: %i" % (i, list[i-1]))
