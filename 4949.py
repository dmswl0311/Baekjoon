from sys import stdin

s = str(stdin.readline().strip())
result = []

while(s != '.'):
    array = []
    flag = 0
    for i in range(len(s)):
        if s[i] == '(' or ')' or '[' or ']':
            if len(array) == 0 and s[i] == '(' or s[i] == '[':
                array.append(s[i])
                print(i, array)
            elif len(array) == 0 and s[i] == ')' or s[i] == ']':
                flag = 1
                break
            elif array[-1] != s[i]:
                if array[-1] == '(' or array[-1] == ')' and s[i] == '[' or s[i] == ']':
                    array.append(s[i])
                    print(i, array)
                elif array[-1] == '[' or array[-1] == ']' and s[i] == '(' or s[i] == ')':
                    array.append(s[i])
                    print(i, array)
                else:
                    array.pop()
                    print(i, array)
            else:
                array.append(s[i])
                print(i, array)
        else:
            continue

    if len(array) == 0 and flag == 0:
        result.append('yes')
    else:
        result.append('no')

    s = str(stdin.readline().strip())

print(result)
