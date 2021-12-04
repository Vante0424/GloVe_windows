f = open('test_true.txt', 'r', encoding='utf-8')
f1 = open('test0.txt', 'w', encoding='utf-8')
i = 0
words = 0
for line in f.readlines():
    line = eval(line)
    str1 = ''
    tokens = line['tokens']
    for token in tokens:
        str1 = str1 + token + ' '
    words += len(tokens)
    f1.write(str1 + '\n')
    i += 1
    if i == 130:
        break

print(words)
