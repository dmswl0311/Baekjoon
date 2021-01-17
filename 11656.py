import sys

s = str(sys.stdin.readline().strip())
a = []

for i in range(len(s)):
    a.append(s[i:])

a.sort()

for i in a:
    print(i)
