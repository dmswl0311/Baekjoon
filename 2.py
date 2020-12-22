data = '1101100100101111001111000000'
penter = '1100'
pescape = '1001'
pexit = '0010'
answer = ''
result = []

for i in range(0, len(data), 4):
    a = data[i:i+4]
    if (a == penter):
        a = pescape+a
    elif(a == pexit):
        a = pescape+a
    elif(a == pescape):
        a = pescape+a
    else:
        a = a
    result.append(a)

for i i
result.insert(0, penter)
result.append(pexit)


print(result)
