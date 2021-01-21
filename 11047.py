from sys import stdin

n, k = map(int, stdin.readline().split())
array = [int(stdin.readline().strip()) for _ in range(n)]
won = k
result = 0

for i in range(n-1, -1, -1):
    cal = 0
    if (array[i] <= won):
        cal = (won//array[i])
        won -= cal*array[i]
        result += cal
    else:
        continue

print(result)
