n, k = map(int, input().split())
cnt = 0

if n < k:
    mok = k//2
    x = mok-n
    n = mok+x
    cnt += x
    cnt += 1
else:
    n = k
    k = n
    mok = k//2
    x = mok-n
    n = mok+x
    cnt += x
    cnt += 1

print(cnt)
