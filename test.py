f1 = open('test_true.txt', 'r', encoding='utf-8')
f2 = open('test_char.txt', 'w', encoding='utf-8')
f3 = open('truth0.txt', 'w', encoding='utf-8')

words = []

i = 0
for line in f1.readlines():
    line = eval(line)
    f3.write(str(line) + '\n')

    tokens = line['tokens']

    for token in tokens:
        words.append(token)

    i += 1
    if i == 130:
        break


for word in words:
    f2.write(str(word) + '\n')

f1.close()
f2.close()
f3.close()

print(len(words))
