t = int(input())
result = []

for i in range(t):
    sum = 0
    a = input().split(',')
    for s in a:
        sum += int(s)
    result.append(sum)

for i in result:
    print(i)
