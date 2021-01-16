n = int(input())
array = [float(input()) for _ in range(n)]

array.sort()

print("%.2f" % (array[1]))
