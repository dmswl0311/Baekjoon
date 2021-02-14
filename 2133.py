n = int(input())
d = [0]*(31)

d[0] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = d[i-2]*3
    if i % 2 == 0:
        d[i] += 2*(d[i-4])

print(d[n])
