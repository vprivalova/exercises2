"""
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
"""

text = input()

cnt = 0
count_values = []

for item in text:
    if item.isspace():
        cnt = cnt + 1
    else:
        count_values.append(cnt)
        cnt = 0

print(max(count_values))
