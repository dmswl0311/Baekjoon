import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    order = i
    result.append((int(age), name, i))

result = sorted(result, key=lambda x: (x[0], x[2]))

for i in result:
    print(i[0], i[1])
