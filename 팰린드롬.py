# 백준 1259 팰린드롬수 코드 간단히

num = input()
result_list = []

while(num != '0'):

    if num[::-1] == num:
        result_list.append('yes')
    else:
        result_list.append('no')
    num = input()

for i in result_list:
    print(i)
