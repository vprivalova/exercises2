"""
Задание 16.
Дан текст. Проверить, правильно ли в нем расставлены круглые скобки (т. е.
находится ли справа от каждой открывающей скобки соответствующая ей закрывающая
скобка, а слева от каждой закрывающей — соответствующаяей закрывающая).
"""

text = input()
text = list(text)
symbols = list(filter(lambda x: x in '()', text))
error = 0

if len(symbols) % 2 != 0:
    print('Круглые скобки расставлены в тексте не корректно')
else:
    for index in range(len(symbols)):
        if index % 2 == 0:
            if symbols[index] != '(':
                error = error + 1
        else:
            if symbols[index] != ')':
                error = error + 1

    if error == 0:
        print('Круглые скобки расставлены в тексте корректно.')
    else:
        print('Круглые скобки расставлены в тексте не корректно.')
