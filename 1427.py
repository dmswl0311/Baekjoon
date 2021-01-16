import sys

s = str(sys.stdin.readline().strip())
array = []

for i in range(len(s)):
    array.append(s[i])


def quick(array, start, end):
    if (end-start <= 0):
        return array
    pivot = start
    left = pivot+1
    right = end

    while(left <= right):
        while(left <= end and array[pivot] <= array[left]):
            left += 1
        while(right > start and array[pivot] >= array[right]):
            right -= 1
        if (left > right):
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[right], array[left] = array[left], array[right]

    quick(array, start, right-1)
    quick(array, right+1, end)


quick(array, 0, len(array)-1)

for i in array:
    print(i, end='')
