"""
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
"""

text = input()

count = 0
symbols = ''
result = ''

for item in text:
    if item not in symbols:
        symbols = symbols + item

list_of_symbols = sorted(symbols)

for elem in list_of_symbols:
    for item in text:
        if item == elem:
            count = count + 1
    if count == 3:
        result = elem
    count = 0

print(result)
