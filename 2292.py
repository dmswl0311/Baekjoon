import sys

N = int(sys.stdin.readline())
cnt = 0
r = 1
i = 0

while(True):
    r = r+(6*i)
    cnt += 1
    if (N <= r):
        print(cnt)
        break
    i += 1
