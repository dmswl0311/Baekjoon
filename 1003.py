t = int(input())
array = [int(input()) for _ in range(t)]

zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(x):
    if len(zero) <= x:
        for j in range(len(zero), x+1):
            zero.append(zero[j-1]+zero[j-2])
            one.append(one[j-1]+one[j-2])

    return print(zero[x], one[x])


for i in array:
    fibo(i)
