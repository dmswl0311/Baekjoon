n = int(input())
ori_n = n
x = 0

while(x <= ori_n):
    sum = 0
    y = x
    y2 = 0
    while(y != 0):
        y2 = y % 10
        y = y//10
        sum += y2
    if ori_n == sum+x:
        print(x)
        break
    else:
        x += 1
        continue

if ori_n != sum+x:
    print('0')
