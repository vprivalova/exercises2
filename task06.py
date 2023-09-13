"""
Задание 6.
Дано предложение. Напечатать его в обратном порядке слов.
"""


sentence = input().split()

punct_sign = str(sentence[-1])[-1]
reverse_sentence = sentence[::-1]
reverse_sentence.pop(0)
reverse_sentence.insert(0, str(sentence[-1])[:-1])
result = ' '.join(reverse_sentence)

if result[-1] != ',':
    print(result.capitalize() + punct_sign)
else:
    print(result[:-1].capitalize() + punct_sign)
