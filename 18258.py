from collections import deque
from sys import stdin


def push(num):
    queue.append(num)


def pop():
    if len(queue) != 0:
        a = queue.popleft()
        print(a)
    else:
        print(-1)


def size():
    print(len(queue))


def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(queue) != 0:
        print(queue[0])
    else:
        print(-1)


def back():
    if len(queue) != 0:
        print(queue[-1])
    else:
        print(-1)


queue = deque()
n = int(stdin.readline())
array = []

for i in range(n):
    c = stdin.readline().split()
    array.append(c)

for i in array:
    if i[0] == 'push':
        push(i[1])
    elif i[0] == 'pop':
        pop()
    elif i[0] == 'size':
        size()
    elif i[0] == 'empty':
        empty()
    elif i[0] == 'front':
        front()
    elif i[0] == 'back':
        back()
    else:
        False
