"""
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
"""


text = input()
count = 0
letters = ''
for item in text:
    if item.isalpha():
        if item not in letters:
            letters = letters + item
list_of_letters = sorted(letters)
print(len(list_of_letters))

