from sys import stdin

n = int(stdin.readline())

array = []
s = []


def push(n):
    s.append(n)


def pop():
    if len(s) == 0:
        print(-1)
    else:
        a = s.pop()
        print(a)


def size():
    print(len(s))


def empty():
    if len(s) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(s) != 0:
        print(s[-1])
    else:
        print(-1)


for i in range(n):
    c = stdin.readline().rstrip().split()
    array.append(c)

for i in range(n):
    if array[i][0] == 'push':
        push(array[i][1])
    elif array[i][0] == 'pop':
        pop()
    elif array[i][0] == 'size':
        size()
    elif array[i][0] == 'empty':
        empty()
    elif array[i][0] == 'top':
        top()
    else:
        print(False)
