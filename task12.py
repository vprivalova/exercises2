"""
Задание 12.
Как известно, имя в языке Python может содержать только латинские символы, цифры
и знак подчеркивания "_". При этом, имя не может начинаться с цифры и не может быть
ключевым словом. Напишите программу, которая проверяет введенную строку, может ли
она быть именем в языке Python.
"""

import keyword

name = input()

VALID_SIGNS = '0123456789_qwertyuioplkjhgfdsazxcvbnm'
cnt = 0

if name[0].isalpha():
    if keyword.iskeyword(name):
        print('Не может быть именем в языке Python')
        cnt = cnt + 1
    else:
        for letter in name:
            if letter not in VALID_SIGNS:
                cnt = cnt + 1
                print('Не может быть именем в языке Python')
                break
else:
    print('Не может быть именем в языке Python')
    cnt = cnt + 1


if cnt == 0:
    print('Может быть именем в языке Python')
