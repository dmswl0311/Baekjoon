from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
array = []
result = []
for i in range(1, n+1):
    array.append(i)

start = 0

while(len(array) != 3):
    if (start+3) < n:
        a = array[start+3]
        array.pop(start+3)
        start = start+3
    else:
        a = array[(start+3)-n-1]
        array.pop((start+3)-n-1)
        start = (start+3)-n-1

    result.append(a)

for i in range(3):
    result.append(array[i])

print(result)
