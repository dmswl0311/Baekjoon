import sys

t = int(sys.stdin.readline())
result = []

for i in range(t):
    num_list = list(map(int, sys.stdin.readline().split()))

    num_list.sort(reverse=True)
    result.append(num_list[2])

for i in result:
    print(i)
