n, k = map(int, input().split())


def factorial(num):
    x = 1
    for i in range(1, num+1):
        x *= i
    return x


result = factorial(n)//(factorial(k)*factorial(n-k))
print(result)
