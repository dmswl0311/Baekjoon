import sys

C = int(sys.stdin.readline())
list_result = []

for i in range(C):
    result = 0
    avg = 0
    sum = 0
    list = [int(x) for x in sys.stdin.readline().strip().split()]
    N = list[0]
    for k in list[1:]:
        avg += k
    avg = avg/(len(list)-1)
    for l in list[1:]:
        if l > avg:
            sum += 1
    result = sum/(len(list)-1)*100
    list_result.append(result)
    del list

for i in list_result:
    print("%.3f%%" % i)
