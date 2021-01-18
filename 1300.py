n = int(input())
k = int(input())
b = []

for i in range(n):
    for j in range(n):
        b.append((i+1)*(j+1))

b.sort()

print(b[k-1])
