import sys

n = int(sys.stdin.readline())
array1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
array2 = list(map(int, sys.stdin.readline().split()))
result = [0]*m

# for i in range(m):
#     for j in range(n):
#         if (array2[i] == array1[j]):
#             result[i] = 1
#             break
#         else:
#             result[i] = 0
#             continue

array1 = sorted(array1)
array2 = sorted(array2)
array3 = array1

print(array1)

for i in range(m):
    if array2[i] <= array3[(len(array3)//2)]:
        array3 = array3[:(len(array3)//2)+1]
        for j in range(len(array3)):
            if (array2[i] == array3[j]):
                result[i] = 1
                break
            else:
                result[i] = 0
                continue
    else:
        array3 = array3[(len(array3)//2)+1:]
        for j in range(len(array3)):
            if (array2[i] == array3[j]):
                result[i] = 1
                break
            else:
                result[i] = 0
                continue

for i in result:
    print(i)
