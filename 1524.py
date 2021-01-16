import sys

t = int(sys.stdin.readline())
j, b = map(int, sys.stdin.readline().split())
power_j = list(map(int, sys.stdin.readline()))
power_b = list(map(int, sys.stdin.readline()))

power_j.sort()
power_b.sort()
array = (power_b+power_j).sort()
if array[0]:
    print("S")

while(병사가 한명 남을때까지):
