import sys

n = int(sys.stdin.readline())
sum = 0
list = []

for i in range(0, n):
    a, b = map(int, sys.stdin.readline().split())
    sum = a+b
    list.append(sum)
for i in range(0, n):
    print(list[i])

# a,b=map(int,sys.stdin.readline().split())
