import sys

n = int(sys.stdin.readline())
array1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array2 = list(map(int, sys.stdin.readline().split()))

array1.sort()


def binary(array, target, start, end):
    if start > end:
        return 0

    mid = (start+end)//2

    if (array[mid] == target):
        return 1
    elif (array[mid] > target):
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)


for i in array2:
    print(binary(array1, i, 0, n-1))
