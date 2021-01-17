import sys

n = int(sys.stdin.readline())
book = [str(sys.stdin.readline().strip()) for _ in range(n)]
count = [0]*n

for i in range(n):
    count[i] = (book[i], book.count(book[i]))

count = sorted(list(set(count)), key=lambda x: (-x[1], x[0]))

print(count[0][0])
