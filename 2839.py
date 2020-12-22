import sys

N = int(sys.stdin.readline())
r = N//3+1
result_1 = "NULL"
result_2 = "NULL"

for i in range(r):
    for j in range(r):
        if (3*i+5*j) == N:
            result_1 = i+j
            break

for i in range(r):
    for j in range(r):
        if (3*j+5*i) == N:
            result_2 = i+j
            break

if (result_1 and result_2) == "NULL":

    print("-1")
elif result_1 > result_2:
    print(result_2)
else:
    print(result_1)
