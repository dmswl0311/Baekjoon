result_list = []

while(True):
    s = input()
    flag = 0
    limit = 0
    if (s == '0'):
        break
    else:
        if (len(s) % 2 != 0):
            limit = (len(s)//2)+1
        else:
            limit = len(s)//2

        for i in range(limit):
            flag = 0
            if(s[i] == s[-(i+1)]):
                flag = 1
            else:
                result_list.append((s, 'no'))
                break

        if (flag == 1):
            result_list.append((s, 'yes'))

for i in result_list:
    print(i[1])
