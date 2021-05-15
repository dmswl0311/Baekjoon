import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
num = str(a*b*c)
cnt = [0]*10

for j in num:
    for i in range(10):
        if j == str(i):
            cnt[int(i)] += 1
        else:
            continue

for i in cnt:
    print(i)
