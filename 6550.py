while(True):
    try:
        s, t = map(str, input().split())
        n = 0
        flag = -1
        for i in range(len(t)):
            if t[i] == s[n]:
                n += 1
                if n == len(s):
                    print("Yes")
                    flag = 0
                    break
        if flag == -1:
            print("No")

    except:
        break
