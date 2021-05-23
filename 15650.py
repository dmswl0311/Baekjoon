import sys
from itertools import combinations

input = sys.stdin.readline

n, r = map(int, input().split())
n_list = []

for i in range(1, n+1):
    n_list.append(i)

l = list(combinations(n_list, r))

for i in range(len(l)):
    for j in range(r):
        print(l[i][j], end=" ")
    print("")
