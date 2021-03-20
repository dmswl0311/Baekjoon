import sys
input = sys.stdin.readline

n = int(input())
s = []
result = 0

for _ in range(n):
    s.append(input().rstrip())

for str in s:
    check = ""
    cnt = 0
    flag = 0
    for i in str:
        if i not in check:
            check = check+i
        elif i in check and check[-1] == i:
            check = check+i
        else:
            flag = -1
            break
    if flag == 0:
        result += 1

print(result)
