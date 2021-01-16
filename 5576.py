# 계수 정렬 사용해서 풀어봄

w = [0]*101
k = [0]*101
result_w = [0]*10
result_k = [0]*10
max = {9, 8, 7}
for i in range(10):
    w[int(input())] += 1

for i in range(10):
    k[int(input())] += 1

a = 0
sum = 0
for i in range(101):
    if(w[i] != 0):
        for j in range(w[i]):
            result_w[a] = i
            if a in max:
                sum += i
            a += 1
    else:
        continue
a = 0
sum2 = 0
for i in range(101):
    if(k[i] != 0):
        for j in range(k[i]):
            result_k[a] = i
            if a in max:
                sum2 += i
            a += 1
    else:
        continue
print(sum, sum2)
