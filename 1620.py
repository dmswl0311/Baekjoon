n, m = map(int, input().split())
array = [input() for _ in range(n)]
problem = [input() for _ in range(m)]

for i in range(m):
    if problem[i].isdigit():
        print(array[int(problem[i])-1])
    else:
        print(array.index(problem[i])+1)
