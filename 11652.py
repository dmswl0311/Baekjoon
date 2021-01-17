import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
count = [0]*n

for i in range(n):
    count[i] = (array[i], array.count(array[i]))

count.sort(key=lambda x: (-x[1], x[0]))

print(count[0][0])
