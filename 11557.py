t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(str, input().split())
        arr.append((a, int(b)))
    arr = sorted(arr, key=lambda x: (x[1], x[0]), reverse=True)
    print(arr[0][0])
