import sys
input = sys.stdin.readline

# 입력받는 문자 뒤에 공백 없애주기 위해 rstrip 사용
doc = input().rstrip()
word = input().rstrip()
cnt = 0
s = 0

while(s <= len(doc)-len(word)):
    if doc[s:s+len(word)] == word:
        cnt += 1
        s += len(word)
    else:
        s += 1

print(cnt)
