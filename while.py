import sys
list = []

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 & B == 0:
        break
    list.append(A+B)

for i in range(len(list)):
    print(list[i])
