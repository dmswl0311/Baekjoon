import sys

k, n = map(int, sys.stdin.readline().split())
array = [int(sys.stdin.readline()) for _ in range(k)]
result = 0

start = 1
end = max(array)

while(start <= end):
    sum = 0
    mid = (start+end)//2

    for i in array:
        sum += (i//mid)

    if sum < n:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
