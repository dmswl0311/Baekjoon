import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

result = 0

for i in range(len(arr)):
    result += sum(arr[:i+1])

print(result)
