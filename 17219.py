from sys import stdin

n, m = map(int, stdin.readline().split())
site = []

for i in range(n):
    url, pwd = map(str, stdin.readline().split())
    site.append((url, pwd))

site.sort()

array = [stdin.readline().rstrip() for _ in range(m)]

for s in array:
    flag = 0
    for i in range(n):
        if s in site[i][0]:
            print(site[i][1])
            flag = 1
        if flag == 1:
            break
