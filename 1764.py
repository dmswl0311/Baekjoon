from sys import stdin

n, m = map(int, stdin.readline().split())
N = sorted([str(stdin.readline().strip()) for _ in range(n)])
M = [str(stdin.readline().strip()) for _ in range(m)]


def binary(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)


result = []
cnt = 0
for i in M:
    if binary(N, i, 0, n-1) == 1:
        cnt += 1
        result.append(i)
print(cnt)
result.sort()
for i in result:
    print(i)
