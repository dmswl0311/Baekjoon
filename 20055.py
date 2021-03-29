import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
# score = 내구도
score = deque(list(map(int, input().split())))
# 로봇의 위치
robot = deque([0]*n)
# 단계 수 세는 변수
cnt = 1

while(True):
    flag = 0
    score.rotate(1)
    robot.rotate(1)
    # 로봇 내려감
    robot[n-1] = 0

    # flag 따로 안쓸려면 뒤에서부터 탐색
    for i in range(n-2, -1, -1):
        if(robot[i] != 0 and robot[i+1] == 0 and score[i+1] >= 1):
            score[i+1] -= 1
            robot[i+1] = robot[i]
            robot[i] = 0
    robot[n-1] = 0

    if robot[0] == 0 and score[0] > 0:
        robot[0] = 1
        score[0] -= 1

    zero_count = 0
    for i in range(len(score)):
        if(score[i] == 0):
            zero_count += 1

    if zero_count >= k:
        print(cnt)
        break
    cnt += 1
