# 단일 target 아님, 중복도 존재 -> 이진탐색이 적합하지 않음

from sys import stdin

n = int(stdin.readline())
a = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))


def binary(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2

    if array[mid] == target:
        return a[start:end+1].count(target)
    elif array[mid] > target:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)


for j in b:
    print(binary(a, j, 0, n-1), end=' ')
