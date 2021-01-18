from sys import stdin

k, n = map(int, stdin.readline().split())
array = [int(stdin.readline()) for _ in range(k)]
result = 0

start = 0
end = max(array)

while(start < end):
    mid = (start+end)//2
    sum = 0

    for i in array:
        if mid < i:
            sum += (i//mid)
    if sum < n:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
