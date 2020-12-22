import sys

A, B, V = map(int, sys.stdin.readline().split())
result = 0
cnt = 0

while (True):
    result += A
    cnt += 1
    if (result == V):
        print(cnt)
        break
    result -= B
