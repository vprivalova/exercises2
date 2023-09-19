"""
Задание 7.
Дано предложение. Найти длину его самого короткого слова.
"""

signs = '.,?!():"'
min_len = 100

sentence = input().split()

for word in sentence:
    for letter in word:
        if letter in signs:
            word = word.replace(letter, '')

for item in sentence:
    if len(item) < min_len:
        min_len = len(item)

print(min_len)
