n = int(input())
a = 0

for i in range(1, n+1):
    print(" "*(n-i), end="")
    if i == n:
        print("*"*n, end="")
        break
    else:
        print("*", end="")
        print(" "*(a+2), end="")
        a = a+2
    print("*")
