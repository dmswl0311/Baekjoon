n, m = map(int, input().split())
c_list = list(map(int, input().split()))
x = 0

for i in range(n-2):
    for k in range(i+1, n):
        start = c_list[i]+c_list[k]
        for j in range(k+1, n):
            if(start+c_list[j] <= m):
                if (x < start+c_list[j]):
                    x = start+c_list[j]
            else:
                continue

print(x)
