import sys

a, b, v = map(int, sys.stdin.readline().split())

day = 1

if (a == v):
    print(day)
else:
    day = (v-a)//(a-b)
    if (v-a) % (a-b) == 0:
        print(day+1)
    else:
        print(day+2)


# 시간초과 코드
# x = 1
# p = 0
# while(True):
#     if (p+a < v):
#         p += a-b
#     else:
#         print(x)
#         break
#     x += 1
