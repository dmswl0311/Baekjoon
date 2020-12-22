import sys
a = []
count = 0

for i in range(9):
    x = int(sys.stdin.readline().rstrip())
    a.append(x)

for i in range(9):
    if a[i] == max(a):
        count = i
    else:
        continue

print(max(a))
print(count+1)
