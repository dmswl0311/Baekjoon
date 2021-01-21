s = input().split('-')
result = []

for i in s:
    cnt = 0
    a = i.split('+')
    for j in a:
        cnt += int(j)
    result.append(cnt)

dap = result[0]

for i in range(1, len(result)):
    dap -= result[i]
print(dap)
