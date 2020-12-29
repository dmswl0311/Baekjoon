result_list = []

T = int(input())
for i in range(T):
    result = ''
    r, s = map(str, input().split())
    r = int(r)
    for j in s:
        result += j*r
    result_list.append(result)

for i in range(T):
    print(result_list[i])
