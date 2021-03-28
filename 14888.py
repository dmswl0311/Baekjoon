import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

flag = ['+', '-', '*', '//']
operation_list = []
n = int(input())
array = list(map(int, input().split()))
f = list(map(int, input().split()))
# 결과가 들어갈 r array
r = []
# 필요한 사칙연산 list 만들기
for i in range(4):
    if f[i] != 0:
        for j in range(f[i]):
            operation_list.append(flag[i])

# 조합 이용해서 가능한 조합 출력하기, set을 이용해서 '+'가 반복되는 등의 중복 제거
case_list = set(permutations(operation_list, n-1))

# 모든 경우의 수 계산
for case in case_list:
    q = deque(array)
    for operation in case:
        result = q.popleft()
        next = q.popleft()
        if operation == "+":
            result = result+next
        elif operation == "-":
            result = result-next
        elif operation == "*":
            result = result*next
        elif operation == "//":
            if result >= 0:
                result = (result)//(next)
            else:
                result = -(result)
                result = (result)//(next)
                result = -(result)
        q.appendleft(result)
    r.append(q.popleft())

print(max(r))
print(min(r))
