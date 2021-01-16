n, i = map(int, input().split())
array = [str(input()) for _ in range(n)]
array.sort()
print(array[i-1])
