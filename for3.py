import sys
N, X = map(int, sys.stdin.readline().split())

a = [int(x) for x in sys.stdin.readline().strip().split()]

for i in a:
    if i < X:
        print(i, end=" ")
