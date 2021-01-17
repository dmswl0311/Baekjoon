# 계수 정렬? 놉
import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]
count = []

for i in range(len(array)):
    count.append((array[i], array.count(array[i])))

count.sort(key=lambda x: x[1], reverse=True)

print(count[0][0])
