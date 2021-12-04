import numpy as np


def split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data[train_indices], data[test_indices]


train_file = 'train_true.txt'
test_file = 'test_true.txt'
f1 = open(train_file, 'w', encoding='utf-8')
f2 = open(test_file, 'w', encoding='utf-8')
with open('groundtruth.txt', 'r', encoding='utf-8') as f:
    train_data, test_data = split_data(np.array(f.readlines()), 0.3)

for line in train_data:
    f1.write(str(line))
for line in test_data:
    f2.write(str(line))

f1.close()
f2.close()

print(len(train_data))
print(len(test_data))
