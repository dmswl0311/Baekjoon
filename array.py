import sys

N = int(sys.stdin.readline())

a = [int(x) for x in sys.stdin.readline().strip().split()]

print(min(a), max(a))
