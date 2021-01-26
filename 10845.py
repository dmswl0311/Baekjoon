from collections import deque
from sys import stdin

q = deque()
result = []


def push(x):
    q.append(x)


def pop():
    if len(q) == 0:
        result.append(-1)
    else:
        a = q.popleft()
        result.append(a)


def size():
    result.append(len(q))


def empty():
    if len(q) == 0:
        result.append(1)
    else:
        result.append(0)


def front():
    if len(q) == 0:
        result.append(-1)
    else:
        result.append(q[0])


def back():
    if len(q) == 0:
        result.append(-1)
    else:
        result.append(q[-1])


n = int(stdin.readline())

for i in range(n):
    c = stdin.readline().split()
    if c[0] == 'push':
        push(c[1])
    elif c[0] == 'pop':
        pop()
    elif c[0] == 'size':
        size()
    elif c[0] == 'empty':
        empty()
    elif c[0] == 'front':
        front()
    elif c[0] == 'back':
        back()

for i in result:
    print(i)
