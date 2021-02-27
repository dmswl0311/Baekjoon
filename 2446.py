n = int(input())
j = n

for i in range(n):
    print(" "*(i), end="")
    print("*"*(j*2-1))
    j -= 1
j = 1
for i in range(n-2, -1, -1):
    print(" "*(i), end="")
    print("*"*(j*2+1))
    j += 1
