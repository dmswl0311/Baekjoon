n = int(input())
word_list = []

for i in range(n):
    word = str(input())
    word_count = len(word)
    word_list.append((word, word_count))

word_list = list(set(word_list))
word_list = sorted(word_list, key=lambda x: (x[1], x[0]))

for x in word_list:
    print(x[0])
