a = int(input())
b = int(input())

x = b % 10
y = ((b-x) % 100)//10
z = (b-x) // 100

print(a*x)
print(a*y)
print(a*z)
print(a*b)
