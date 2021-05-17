import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
cnt = 0

for _ in range(n):
    s.append(input().rstrip())

for _ in range(m):
    sentence = input().rstrip()
    if sentence in s:
        cnt += 1

print(cnt)
