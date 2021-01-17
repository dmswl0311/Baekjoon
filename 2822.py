import sys

array = [0]*8

for i in range(8):
    array[i] = (int(sys.stdin.readline()), i+1)

array.sort(key=lambda x: x[0], reverse=True)
result = sorted(array[:5], key=lambda x: x[1])
sum = 0
for i in result:
    sum += i[0]
print(sum)
for i in result:
    print(i[1], end=' ')
