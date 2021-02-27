# 뒤에 공백 없앰

n = int(input())
a = 1

for i in range(n-1, -1, -1):
    print(" "*(i), end="")
    print("*"*(2*a-1))
    a += 1
