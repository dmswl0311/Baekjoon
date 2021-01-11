a, b, c = map(int, input().split())
d = int(input())

hour = a+(d//3600)
min = b+((d % 3600)//60)
sec = c+(d % 3600) % 60

if sec >= 60:
    min += 1
    sec = sec % 60

if min >= 60:
    hour += 1
    min = min % 60

if hour >= 24:
    hour = hour % 24

print(hour, min, sec)
