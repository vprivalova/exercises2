"""
Задание 2.
Дан текст. Необходимо определить максимальное количество последовательных одинаковых символов в нём.
"""

text = input()

cnt = 0
count_values = []

for index in range(len(text) - 1):
    if text[index] == text[index + 1]:
        cnt = cnt + 1
    else:
        count_values.append(cnt)
        cnt = 0

print(max(count_values) + 1)
