n = int(input())
array = list(map(int, input().split()))
sum = [array[0]]

for i in range(n-1):
    sum.append(max(sum[i]+array[i+1], array[i+1]))

print(max(sum))
