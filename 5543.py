import sys

list_ham = []
list_drink = []
result_ham = 0
result_drink = 0

for i in range(3):
    list_ham.append(int(sys.stdin.readline()))
    result_ham = min(list_ham)

for i in range(2):
    list_drink.append(int(sys.stdin.readline()))
    result_drink = min(list_drink)

print(result_ham+result_drink-50)
