n = 0
result = []
while True:
    try:
        a, b = map(int, input().split())
        result.append(a+b)
        n += 1
    except:
        break

for i in range(n):
    print(result[i])
