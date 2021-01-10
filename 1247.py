import sys

result = [0]*3
sum = 0

for i in range(3):
    n = int(sys.stdin.readline())
    for _ in range(n):
        num = int(sys.stdin.readline())
        sum += num
        if (sum > 0):
            result[i] = '+'
        elif (sum < 0):
            result[i] = '-'
        elif(sum == 0):
            result[i] = '0'
    sum = 0

for i in result:
    print(i)
