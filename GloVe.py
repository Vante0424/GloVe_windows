from time import *
import sklearn.svm as svm
import numpy as np

start_time = time()
print(start_time)
glove_file = '/data/home/wangyuxiao/GloVe_win/glove.840B.300d.txt'

glove = dict()
total_vector_words = []
with open(glove_file, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip().split()
        glove[line[0]] = np.array(line[1:], dtype=float)
        total_vector_words.append(str(line[0]))
glove_dict_time = time()
print('加载GloVe用时：', format(glove_dict_time - start_time))

train_y = []
with open('train_y.txt', 'r', encoding='utf-8') as f:
    for label in f.readlines():
        label = label.strip()
        train_y.append(label)

f1 = open('train_char.txt', 'r', encoding='utf-8')
f2 = open('train_x.txt', 'w', encoding='utf-8')

train_x = []
for line in f1.readlines():
    line = line.strip('\n')
    if line in total_vector_words:
        f2.write(str(glove[line]) + '\n')
        train_x.append(glove[line])
    elif line.lower() in total_vector_words:
        f2.write(str(glove[line.lower()]) + '\n')
        train_x.append(glove[line.lower()])
    else:
        feature = np.random.uniform(-1/300, 1/300, 300)
        f2.write(str(feature) + '\n')
        train_x.append(feature)
f1.close()

PAD = np.random.uniform(-1/300, 1/300, 300)
train_x_win = []
for i in range(len(train_x)):
    if i == 0:
        train_x_win.append(train_x[i]
                           + train_x[i + 1]
                           + train_x[i + 2]
                           + PAD + PAD)
    elif i == 1:
        train_x_win.append(train_x[i]
                           + train_x[i + 1]
                           + train_x[i - 1]
                           + train_x[i + 2]
                           + PAD)
    elif i == len(train_x)-2:
        train_x_win.append(train_x[i]
                           + train_x[i + 1]
                           + train_x[i - 1]
                           + train_x[i - 2]
                           + PAD)
    elif i == len(train_x)-1:
        train_x_win.append(train_x[i]
                           + train_x[i - 1]
                           + train_x[i - 2]
                           + PAD + PAD)
    else:
        train_x_win.append(train_x[i]
                           + train_x[i + 1]
                           + train_x[i - 1]
                           + train_x[i + 2]
                           + train_x[i - 2])

f2.close()

test_x = []
f4 = open('test_char.txt', 'r', encoding='utf-8')
for line in f4.readlines():
    line = line.strip()
    if line not in glove:
        test_x.append(np.random.uniform(-1/300, 1/300, 300))
    else:
        test_x.append(np.array(glove[line], dtype=float))

print(len(train_x))
print(len(train_y))
print(len(test_x))


# train
svm_model = svm.SVC(kernel='rbf', verbose=True, C=100)
svm_model.fit(train_x_win, train_y)

test_y = svm_model.predict(test_x)
# print(test_y)
print(len(test_y))

svm_time = time()
print('训练SVM用时：', format(svm_time - glove_dict_time))

if len(test_y) != len(test_x):
    print('ERROR!')
else:
    print('Begin BIO...')
    f_ = open('test0.txt', 'r', encoding='utf-8')
    f_rst = open('final0.txt', 'w', encoding='utf-8')

    i = 0
    for line in f_.readlines():
        # print('i ------ ', format(i))
        line = line.strip()
        final_rst = dict()
        labels = []

        tokens = line.split()
        final_rst['tokens'] = tokens

        for j in range(len(tokens)):
            # print('j=', format(j))
            # print(i+j)
            labels.append(test_y[i + j - 1])

        i += len(tokens) - 1

        final_rst['labels'] = labels
        f_rst.write(str(final_rst) + '\n')

        if i > len(test_y):
            print('ERROR!')
            break
        i += 1

    f_rst.close()
    print('BIO Done!')

end_time = time()
print(end_time)
print('总用时：', format(end_time - start_time))
print('Good Job!')
