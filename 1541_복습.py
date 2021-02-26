s = input().split('-')
sum = 0
result = []

for i in s:
    if '+' in i:
        a = i.split('+')
        for j in a:
            sum += int(j)
        result.append(sum)
    else:
        result.append(int(i))

minus = result[0]

for i in range(1, len(result)):
    minus -= result[i]

print(minus)
