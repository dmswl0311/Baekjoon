import sys

n = int(sys.stdin.readline())
a = [0]*n
for i in range(n):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    a[i] = (name, int(kor), int(eng), int(math))

a.sort(key=lambda x: (x[0]))
a.sort(key=lambda x: (x[3]), reverse=True)
a.sort(key=lambda x: (x[2]))
a.sort(key=lambda x: (x[1]), reverse=True)

for i in a:
    print(i[0])
