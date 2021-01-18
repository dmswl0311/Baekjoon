from sys import stdin

n, m = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))
result = 0

start = 0
end = max(array)

while(start <= end):
    mid = (start+end)//2
    sum = 0
    for x in array:
        if x > mid:
            sum += x-mid

    if sum < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
