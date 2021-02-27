s = input()
start = 0
end = 10

while(len(s) >= 10):
    print(s[:10])
    s = s[10:]

print(s)
