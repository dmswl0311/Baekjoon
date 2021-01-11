# e=대각선 길이 h=높이 비율 w=너비 비율
# x는 비율
import math
e, h, w = map(float, input().split())

x = math.sqrt((e*e)/((h*h)+(w*w)))
h = h*x
w = w*x
print('%d %d' % (h, w))
