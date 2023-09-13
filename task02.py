"""
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
"""


text = input()
count = 0
count_values = []
for index in range(len(text) - 1):
    if text[index] == text[index + 1]:
        count = count + 1
    else:
        count_values.append(count)
        count = 0
print(max(count_values) + 1)
