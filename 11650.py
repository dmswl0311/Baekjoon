import sys

n = int(sys.stdin.readline())
list = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    list.append((x, y))

list = sorted(list, key=lambda x: (x[0], x[1]))

for i in list:
    print(i[0], i[1])
