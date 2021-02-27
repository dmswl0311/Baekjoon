x, y = map(int, input().split())
day = 0

array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

if x != 1:
    for i in range(x-1):
        day += array[i]
    print(weekList[((day+y) % 7)])

else:
    print(weekList[(y % 7)])
