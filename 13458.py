import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0

for i in range(len(a)):
    if a[i]-b >= 0:
        a[i] = a[i]-b
        cnt += 1
i = 0
while(sum(a) > 0):
    if i == len(a):
        i = 0
    if a[i] != 0:
        if a[i]-c >= 0:
            a[i] = a[i]-c
            cnt += 1
        else:
            a[i] = 0
            cnt += 1
    else:
        continue
    i = i+1

print(cnt)
