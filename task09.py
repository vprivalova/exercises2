"""
Задание 9.
Дано предложение. В нем только два слова одинаковые. Найти эти слова.
"""

SIGNS = '.,?!():"'

sentence = input().split()

for word in range(len(sentence)):
    for index in range(len(sentence[word])):
        if (sentence[word])[index] in SIGNS:
            sentence[word] = sentence[word].replace((sentence[word])[index], '')

for item in range(len(sentence)):
    sentence[item] = sentence[item].lower()

for elem in sentence:
    if sentence.count(elem) == 2:
        result = elem

print(result)
