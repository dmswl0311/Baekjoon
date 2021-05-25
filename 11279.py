"""
heappop을 하면 heap에서의 최소값을 삭제하기 때문에 
heap에 원소를 넣을 때 - 부호로 바꿔서 넣어주고, 
출력할때 다시 -를 붙여서 출력시켜주면
최대값을 삭제할 수 있음
"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(h, -num)
    else:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
