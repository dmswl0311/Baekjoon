n = int(input())
start = 666
end = 6660
cnt = 0

result = start + 1000*n

for i in range(len(str(result))):
    if str(result)[i] == '6':
        cnt += 1
    if cnt >= 4:
        result = end + 10000*n
    else:
        break

print(result)
