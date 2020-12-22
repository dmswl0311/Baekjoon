import sys

n = int(sys.stdin.readline())  # 테스트 케이스 개수
list_result = []  # 점수를 저장 할 list_result
text = ""

for i in range(n):
    sum = 0
    score = 0
    list = [x for x in sys.stdin.readline().strip().split()]
    text = str(list)

    for i in text:
        if i == "O":
            score += 1
            sum += score
        else:
            score = 0

    list_result.append(sum)

for i in list_result:
    print(i)
