import sys
n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

result = list(set(num_list))
result = sorted(result, key=lambda x: x)

for i in result:
    print(i)
