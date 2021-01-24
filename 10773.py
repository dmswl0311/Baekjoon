from sys import stdin

k = int(stdin.readline())
s = []
for i in range(k):
    num = int(stdin.readline().strip())
    if num != 0:
        s.append(num)
    elif num == 0:
        s.pop()

print(sum(s))
