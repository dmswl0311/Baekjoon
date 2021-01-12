l = int(input())
s = str(input())
h = 0
k = 0
r = 1

for i in s:
    h += (ord(i)-96)*r
    r *= 31
    k += 1

print(h % 1234567891)
