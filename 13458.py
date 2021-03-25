# 100개의 방, 각 방마다 100개의 사람, 감독관은 각각 1명씩만 볼 수 있을 때 생각해보기

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(len(a)):
    if a[i]-b >= 0:
        a[i] = a[i]-b
    else:
        a[i] = 0
    cnt += 1

    if a[i] > 0:
        if a[i] <= c:
            cnt += 1
        else:
            if(a[i] % c != 0):
                cnt += (a[i]//c)+1
            else:
                cnt += (a[i]//c)

print(cnt)
