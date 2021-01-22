x, y, w, h = map(int, input().split())

next = min(y, h-y, x, w-x)

print(next)
