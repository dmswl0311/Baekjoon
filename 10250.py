import sys

cnt = 0
num = ""
width = ""
height = ""
list = []


def cal(W, H, N):
    global width
    global height
    global num
    global cnt
    global list

    for i in range(1, W+1):
        if i < 10:
            width = "0"+str(i)
        else:
            width = str(i)
        for j in range(1, H+1):
            num = str(j)+width
            cnt += 1
            if cnt == N:
                list.append(num)
                width = ""
                height = ""
                num = ""
                break
    return list


T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    cal(W, H, N)
    cnt = 0

for i in list:
    print(i)
