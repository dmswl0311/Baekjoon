a, b, c = map(int, input().split())
result = []
x, y = 0, 0

while(a != 0 and b != 0 and c != 0):
    max_num = max(a, b, c)
    if (max_num == a):
        x = b
        y = c
    elif (max_num == b):
        x = a
        y = c
    else:
        x = a
        y = b

    if ((max_num**2) == (x**2)+(y**2)):
        result.append('right')
    else:
        result.append('wrong')
    a, b, c = map(int, input().split())

for i in result:
    print(i)
