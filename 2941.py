import sys
input = sys.stdin.readline

s = input().rstrip()
alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# 입력한 문자열 s에 alpha에 있는 문자가 포함될 경우 * 로 replace
for t in alpha:
    s = s.replace(t, "*")

print(len(s))
