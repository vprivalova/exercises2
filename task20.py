"""
Задание 20.
Дано натуральное число не превосходящее 900 000 000. Напишите программу, которая
выводит на экран это число русскими словами.
"""

ONES = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

TEENS = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать',
         'восемнадцать', 'девятнадцать']

TENS = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
        'девяносто']

HUNDREDS = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

THOUSANDS = ['', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч', 'семь тысяч',
             'восемь тысяч', 'девять тысяч']

nmbr = int(input())

if len(str(nmbr)) == 1:
    print(ONES[nmbr])

elif len(str(nmbr)) == 2:
    if (nmbr > 10) and (nmbr < 20):
        print(TEENS[nmbr % 10])
    else:
        print(TENS[nmbr // 10], ONES[nmbr % 10])

elif len(str(nmbr)) == 3:
    if (int(str(nmbr)[1:3]) > 10) and (int(str(nmbr)[1:3]) < 20):
        print(HUNDREDS[nmbr // 100], TEENS[nmbr % 10])
    else:
        print(HUNDREDS[nmbr // 100], TENS[(nmbr % 100) // 10], ONES[nmbr % 10])

elif len(str(nmbr)) == 4:
    pass
elif len(str(nmbr)) == 5:
    pass
elif len(str(nmbr)) == 6:
    pass
elif len(str(nmbr)) == 7:
    pass
elif len(str(nmbr)) == 8:
    pass
elif len(str(nmbr)) == 9:
    pass
