n, l, k = map(int, input().split())
array = []
sum = 0
count = 1
for i in range(n):
    sub1, sub2 = map(int, input().split())
    array.append((sub1, sub2))

array.sort(key=lambda x: (x[1], x[0]))

for i in array:
    if count > k:
        break
    if (i[0] <= l):
        sum += 100
        if (i[1] <= l):
            sum += 40
        count += 1

print(sum)
