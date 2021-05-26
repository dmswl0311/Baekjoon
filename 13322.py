import sys
input = sys.stdin.readline

s = input().rstrip()
l = []
for i in range(len(s)):
    l.append((s[i:], i))

l.sort()

for i in l:
    print(i[1])
