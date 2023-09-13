"""
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
"""


ptr = input()
count = 0
count_values = []
for item in ptr:
    if item.isspace():
        count = count + 1
    else:
        count_values.append(count)
        count = 0
print(max(count_values))




