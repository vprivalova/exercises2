"""
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
"""

signs = '.,?!():"'

sentence = input().split()

for word in range(len(sentence)):
    for index in range(len(sentence[word])):
        if (sentence[word])[index] in signs:
            sentence[word] = sentence[word].replace((sentence[word])[index], '')

print(sentence)
print(*sorted(sentence, key=len))
