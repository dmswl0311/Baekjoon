import sys
list = []
list2 = []
count = 10

for i in range(10):
    x = int(sys.stdin.readline().rstrip())
    list.append(x)

for i in list:
    y = i % 42
    list2.append(y)

for i in range(9):
    for j in range(9):
        if list2[i] == list2[j]:
            count = count - 1
            break
        else:
            continue

print(count)
