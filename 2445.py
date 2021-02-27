n = int(input())
j = n
for i in range(1, n+1):
    print("*"*i, end="")
    print(" "*(2*j-2), end="")
    j -= 1
    print("*"*i)
j = 1
for i in range(n-1, -1, -1):
    print("*"*i, end="")
    print(" "*(2*j), end="")
    j += 1
    print("*"*i)
