result = []

while True:
    try:
        n = int(input())
        d = [0]*251
        d[0] = 1
        d[1] = 1
        d[2] = 3
        d[3] = 5

        for i in range(4, n+1):
            d[i] = d[i-1]+d[i-2]*2

        result.append(d[n])
    except:
        break

for i in result:
    print(i)
