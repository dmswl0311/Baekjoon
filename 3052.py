list = []
cnt = 0
for i in range(10):
    n = int(input())
    result = n % 42
    list.append(result)

for i in range(10):
    for j in range(1, 10-i):
        if list[i] == list[i+j]:
            cnt += 1
            break
print(10-cnt)
