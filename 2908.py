import sys
A, B = map(int, sys.stdin.readline().split())
text = ""
text = str(A)
text2 = ""
text2 = str(B)
text_1 = ""
text_2 = ""

for i in text[::-1]:
    text_1 += i
for i in text2[::-1]:
    text_2 += i


if int(text_1) > int(text_2):
    print(text_1)
else:
    print(text_2)
