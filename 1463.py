x = int(input())
cnt = 0

if x >= 3:
    while(x != 1):
        while(x % 3 != 0):
            x -= 1
            cnt += 1
        x = x//3
        cnt += 1

elif:
    while(x != 1):
        while(x % 2 != 0):
            x -= 1
            cnt += 1
        x = x//2
        cnt += 1

print(cnt)
