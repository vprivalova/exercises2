"""
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
"""

sentence = input().split()

SIGNS = '.,?!():"'
min_len = 100

for word in range(len(sentence)):
    for index in range(len(sentence[word])):
        if (sentence[word])[index] in SIGNS:
            sentence[word] = sentence[word].replace((sentence[word])[index], '')

for item in sentence:
    if len(item) < min_len:
        min_len = len(item)

print(min_len)
