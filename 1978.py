import sys
input = sys.stdin.readline

n = int(input())
num_array = list(map(int, input().split()))
cnt = 0

for i in num_array:
    flag = 0
    if i != 1:
        for j in range(2, i):
            if i % j != 0:
                continue
            else:
                flag = 1
                break
        if flag == 0:
            cnt += 1
    else:
        continue

print(cnt)
