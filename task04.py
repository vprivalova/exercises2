"""
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
"""

text = input()

cnt = 0
symbols = ''
result = ''

for item in text:
    if item not in symbols:
        symbols = symbols + item  # All unique symbols from the tetxt.

list_of_symbols = sorted(symbols)

for elem in list_of_symbols:
    for item in text:
        if item == elem:
            cnt = cnt + 1
    if cnt == 3:
        result = elem
    cnt = 0

print(result)
