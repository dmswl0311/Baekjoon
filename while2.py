N = int(input())
result = 0
Y = N

while True:
    x = Y//10
    y = Y % 10
    X = (x+y) % 10
    hap = y*10+X
    Y = hap
    result = result+1
    if Y != N:
        continue
    else:
        break

print(result)
