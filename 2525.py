a, b = map(int, input().split())
c = int(input())
m = b+c
if (m >= 60):
    a = a+(m//60)
    if (a >= 24):
        a = 0+(a-24)
    b = m % 60
    print(a, b)

elif (c < 60) and (m < 60):
    print(a, b+c)
