# 정렬
# sw 마에스트로 문제

import sys

n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))

house.sort()

median = (n//2)-1

print(house[median])
