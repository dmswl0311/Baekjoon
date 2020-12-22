import sys

V, A, B = map(int, sys.stdin.readline().split())
result = 0
cnt = 1

while (result == V):
    result += A
    result -= B
    cnt += 1

print(cnt)
