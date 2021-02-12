from sys import stdin

m = int(stdin.readline())
array = []


def add(x):
    if x not in array:
        array.append(x)


def remove(x):
    if x in array:
        array.remove(x)


def check(x):
    if x in array:
        return True
    else:
        return False


def toggle(x):
    if x in array:
        array.remove(x)
    else:
        array.append(x)


qq = []

for _ in range(m):
    s = stdin.readline().rstrip().split()
    if s[0] == "add":
        add(int(s[1]))
    elif s[0] == "remove":
        remove(int(s[1]))
    elif s[0] == "check":
        check(int(s[1]))
        if check(int(s[1])) == True:
            qq.append(1)
        else:
            qq.append(0)
    elif s[0] == "toggle":
        toggle(int(s[1]))
    elif s[0] == "all":
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    elif s[0] == "empty":
        array.clear()

for i in qq:
    print(i)
