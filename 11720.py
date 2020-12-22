import sys
N = int(sys.stdin.readline())
sum = 0

data = [int(x) for x in sys.stdin.readline().strip()]

for i in data:
    sum += i
print(sum)
