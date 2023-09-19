"""
Задание 10.
Дано предложение. Выведите на экран те слова, которые отличны от первого слова и
в слове нет повторяющихся букв.
"""

signs = '.,?!():"'
line = ''
count = 0
result = []

sentence = input().split()

for word in range(len(sentence)):
    for index in range(len(sentence[word])):
        if (sentence[word])[index] in signs:
            sentence[word] = sentence[word].replace((sentence[word])[index], '')

for item in range(len(sentence)):
    sentence[item] = sentence[item].lower()

first_word = sentence[0]

sentence = list(filter(lambda x: x != first_word, sentence))

for elem in sentence:
    for letter in elem:
        if letter not in line:
            line = line + letter
        elif letter in line:
            count = count + 1
    if count == 0:
        result.append(elem)
    count = 0
    line = ''


print(*set(result))
