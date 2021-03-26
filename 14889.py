import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
array = [[] for _ in range(n)]
com_array = []
result = []

for i in range(n):
    num_list = list(map(int, input().split()))
    array[i] = num_list

for i in range(0, n):
    com_array.append(i)

hubo = list(combinations(com_array, n//2))

for i in range((len(hubo)//2)+1):
    hap = 0
    hap2 = 0

    team = hubo[i]
    for j in range(n//2):
        member = team[j]
        for k in team:
            hap += array[member][k]
    team = hubo[-i-1]
    for j in range(n//2):
        member = team[j]
        for k in team:
            hap2 += array[member][k]
    if hap >= hap2:
        result.append(hap-hap2)
    else:
        result.append(hap2-hap)

print(min(result))
