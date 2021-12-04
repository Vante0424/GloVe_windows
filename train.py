f1 = open('train_true.txt', 'r', encoding='utf-8')
f2 = open('train_char.txt', 'w', encoding='utf-8')
f3 = open('train_y.txt', 'w', encoding='utf-8')

words = []
labels_total = []

i = 0
for line in f1.readlines():
    line = eval(line)

    tokens = line['tokens']
    labels = line['labels']

    for token in tokens:
        words.append(token)
    for label in labels:
        labels_total.append(label)

    i += 1
    if i == 500:
        break


for word in words:
    f2.write(str(word) + '\n')
for label in labels_total:
    f3.write(str(label) + '\n')

f1.close()
f2.close()
f3.close()

print(len(words))
print(len(labels_total))
