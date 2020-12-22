import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
result = A*B*C
text = ""

text += str(result)

for t in range(0, 10):
    print(text.count(str(t)))
