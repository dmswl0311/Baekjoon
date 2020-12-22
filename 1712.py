import sys

a, b, c = map(int, sys.stdin.readline().split())
cnt = 0

if b >= c:
    cnt = -1

else:
    while(True):
        cnt += 1
        price = a+(b*cnt)
        result_price = (c*cnt)
        if result_price > price:
            break

print(cnt)
