import sys
N = int(sys.stdin.readline())
score = [int(x) for x in sys.stdin.readline().strip().split()]
M = max(score)
score2 = []
sum = 0

for i in score:
    i = i/M*100
    score2.append(i)

for i in score2:
    sum += i

print(sum/N)
