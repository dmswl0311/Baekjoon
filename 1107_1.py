def solution(s, op):
    answer = []
    a = ''
    b = ''
    result = 0

    for i in range(len(s)-1):
        a = s[:i+1]
        b = s[i+1:]
        if (op == "+"):
            result = int(a)+int(b)
        elif (op == "-"):
            result = int(a)-int(b)
        else:
            result = int(a)*int(b)

        answer.append(result)

    return answer


s = "1234"
op = "+"
# aa = len(s)
# a = s[:1]
# b = s[1:]
# c = s[:2]
# d = s[2:]
# e = s[:3]
# f = s[3:]
# print(aa, a, b, c, d, e, f)
print(solution(s, op))
