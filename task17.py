"""
Задание 17.
Строка содержит арифметическое выражение, в котором используются круглые скобки,
в том числе вложенные. Напишите программу, которая вычисляет значение этого выражения.
Функцию eval() не использовать.
"""

task = input()
task = list(task)
symbols = list(filter(lambda x: x in '()+-*/1234567890', task))
print(symbols)
max_ind_lft = 0
max_ind_rght = 0
result = 0
cnt = symbols.count('(')

for i in range(len(symbols)):
    if symbols[i] == '(':
        max_ind_lft = i
for j in range(max_ind_lft, 100000):
    if symbols[j] == ')':
        max_ind_rght = j



