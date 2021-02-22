n = int(input())
sum = 1

for i in range(2, n+1):
    sum *= i

sum = str(sum)
result = 0
flag = 0

for i in range(len(sum)-1, -1, -1):
    if flag == 0:
        if sum[i] == '0':
            result += 1
            flag = 1
    else:
        if sum[i] == '0':
            result += 1
        else:
            break

print(result)
