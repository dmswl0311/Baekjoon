import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

print("%.f" % (round(sum(a)/n, 0)))
a.sort()
print(a[n//2])
result = [0]*n
result2 = []

for i in range(n):
    result[i] = (a[i], a.count(a[i]))

count = 0
result = list(set(result))
result.sort(key=lambda x: (x[0]))
result.sort(key=lambda x: (x[1]), reverse=True)

m = result[0][1]  # 최빈값 빈도수

for i in range(n):
    if (result[i][1] == m):
        result2.append(result[i][0])
        count += 1
    else:
        continue
    if count == 2:
        break

print(result2[-1])
print(a[-1]-a[0])
