from sys import stdin

t = int(stdin.readline())
result = ['NO']*t

for i in range(t):
    s = []
    flag = 0
    array = list(map(str, stdin.readline().strip()))
    for j in range(len(array)):
        if len(s) == 0 and array[j] == '(':
            s.append(array[j])
        elif len(s) == 0 and array[j] == ')':
            flag = 1
            break
        else:
            if array[j] != s[-1]:
                s.pop()
            else:
                s.append(array[j])

    if len(s) == 0 and flag == 0:
        result[i] = 'YES'

for i in result:
    print(i)
