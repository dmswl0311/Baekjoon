import sys

s = sys.stdin.readline().upper()
flag = 0
list = []
list2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
result = ""

for i in list2:
    list.append(s.count(i))

for i in range(len(list)):
    if list[i] == max(list):
        result = list2[i]
        flag += 1

if flag == 1:
    print(result)
else:
    print("?")
