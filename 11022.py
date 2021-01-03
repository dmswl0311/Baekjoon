t = int(input())
a_result = []
b_result = []
result = []

for i in range(t):
    a, b = map(int, input().split())
    result.append(a+b)
    a_result.append(a)
    b_result.append(b)

for i in range(t):
    print("Case #{0}: {1} + {2} = {3}".format(i +
                                              1, a_result[i], b_result[i], result[i]))
