a, b, c = map(int, input().split())
max = max(a, b, c)

if ((a == b) and (b == c) and (c == a)):
    print(10000+(a*1000))
elif(a == b):
    if(c != a):
        print(1000+(a)*100)
    else:
        print(10000+(a*1000))
elif(b == c):
    if(b != a):
        print(1000+(b)*100)
    else:
        print(10000+(b*1000))
elif(a == c):
    if(c != b):
        print(1000+(a)*100)
    else:
        print(10000+(a*1000))
else:
    print((max*100))
