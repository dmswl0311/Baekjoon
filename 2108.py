import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
result = [0]*n

print("%.f" % (round(sum(a)/n, 0)))  # 산술평균

a.sort()
print(a[n//2])  # 중앙값

for i in range(n):
    result[i] = (a[i], a.count(a[i]))

result = list(set(result))
result.sort(key=lambda x: (-x[1], x[0]))

end = 0
for i in range(1, n):
    if (result[i][1] == result[i-1][1]):
        end = i
    else:
        break
result = result[:end+1]

print(result[1][0])
print(a[-1]-a[0])  # 범위
