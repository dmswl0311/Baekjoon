import sys

N = int(sys.stdin.readline())
cnt = 0
flag = 0
list = [int(x) for x in sys.stdin.readline().strip().split()]
list2 = []
for i in list:
    for j in range(2, i):
        if i % j != 0:
            flag = 1
        else:
            break
    if flag == 1:
        cnt += 1
        flag = 0
    if i == 2:
        cnt += 1
print(cnt)

# 왜 9가 소수로 나올까
