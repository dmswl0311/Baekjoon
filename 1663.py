import sys
input = sys.stdin.readline

num = int(input())
n = int(input())
k = input()

count = 0
s = "X"
result = ""
while(True):
    if count == n-1:
        break
    for i in s:
        if i == "X":
            result += "YZ"
        elif i == "Y":
            result += "Z"
        elif i == "Z":
            result += "X"
    s = result
    result = ""
    count += 1

if num == 1:
    print(len(s))

if num == 2:
    k = int(k)
    print(s[k-1])

elif num == 3:
    print(s.count(k))
