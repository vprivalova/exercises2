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

thousand = ' тысяч '
million = ' миллионов '
f_part = ''
s_part = ''
z_part = ''

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
    if (int(str(nmbr)[2:4]) > 10) and (int(str(nmbr)[2:4]) < 20):
        print(THOUSANDS[nmbr // 1000], HUNDREDS[(nmbr % 1000) // 100], TEENS[nmbr % 100])
    else:
        print(THOUSANDS[nmbr // 1000] + ' ' + HUNDREDS[(nmbr % 1000) // 100] + ' ' + TENS[(nmbr % 100) // 10]
              + ' ' + ONES[nmbr % 10])

elif len(str(nmbr)) == 5:
    nmbr1 = int(str(nmbr)[0:2])
    if (nmbr1 > 10) and (nmbr1 < 20):
        f_part = TEENS[nmbr1 % 10]
    else:
        f_part = TENS[nmbr1 // 10] + ' ' + ONES[nmbr1 % 10]

    nmbr2 = int(str(nmbr)[2:5])
    if (int(str(nmbr2)[1:3]) > 10) and (int(str(nmbr2)[1:3]) < 20):
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TEENS[nmbr2 % 10]
    else:
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TENS[(nmbr2 % 100) // 10] + ' ' + ONES[nmbr2 % 10]

    print(f_part + thousand + s_part)

elif len(str(nmbr)) == 6:
    nmbr1 = int(str(nmbr)[0:3])
    if (int(str(nmbr1)[1:3]) > 10) and (int(str(nmbr1)[1:3]) < 20):
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TEENS[nmbr1 % 10]
    else:
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TENS[(nmbr1 % 100) // 10] + ' ' + ONES[nmbr1 % 10]

    nmbr2 = int(str(nmbr)[3:6])
    if (int(str(nmbr2)[1:3]) > 10) and (int(str(nmbr2)[1:3]) < 20):
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TEENS[nmbr2 % 10]
    else:
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TENS[(nmbr2 % 100) // 10] + ' ' + ONES[nmbr2 % 10]

    print(f_part + thousand + s_part)

elif len(str(nmbr)) == 7:
    nmbr0 = int(str(nmbr)[0])
    z_part = ONES[nmbr0]

    nmbr1 = int(str(nmbr)[1:4])
    if (int(str(nmbr1)[1:3]) > 10) and (int(str(nmbr1)[1:3]) < 20):
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TEENS[nmbr1 % 10]
    else:
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TENS[(nmbr1 % 100) // 10] + ' ' + ONES[nmbr1 % 10]

    nmbr2 = int(str(nmbr)[4:7])
    if (int(str(nmbr2)[1:3]) > 10) and (int(str(nmbr2)[1:3]) < 20):
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TEENS[nmbr2 % 10]
    else:
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TENS[(nmbr2 % 100) // 10] + ' ' + ONES[nmbr2 % 10]

    print(z_part + million + f_part + thousand + s_part)

elif len(str(nmbr)) == 8:
    nmbr0 = int(str(nmbr)[0:2])
    if (nmbr0 > 10) and (nmbr0 < 20):
        z_part = TEENS[nmbr0 % 10]
    else:
        z_part = TENS[nmbr0 // 10] + ' ' + ONES[nmbr0 % 10]

    nmbr1 = int(str(nmbr)[2:5])
    if (int(str(nmbr1)[1:3]) > 10) and (int(str(nmbr1)[1:3]) < 20):
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TEENS[nmbr1 % 10]
    else:
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TENS[(nmbr1 % 100) // 10] + ' ' + ONES[nmbr1 % 10]

    nmbr2 = int(str(nmbr)[5:8])
    if (int(str(nmbr2)[1:3]) > 10) and (int(str(nmbr2)[1:3]) < 20):
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TEENS[nmbr2 % 10]
    else:
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TENS[(nmbr2 % 100) // 10] + ' ' + ONES[nmbr2 % 10]

    print(z_part + million + f_part + thousand + s_part)

elif len(str(nmbr)) == 9:
    nmbr0 = int(str(nmbr)[0:3])
    if (int(str(nmbr0)[1:3]) > 10) and (int(str(nmbr0)[1:3]) < 20):
        z_part = HUNDREDS[nmbr0 // 100] + ' ' + TEENS[nmbr0 % 10]
    else:
        z_part = HUNDREDS[nmbr0 // 100] + ' ' + TENS[(nmbr0 % 100) // 10] + ' ' + ONES[nmbr0 % 10]

    nmbr1 = int(str(nmbr)[1:4])
    if (int(str(nmbr1)[3:6]) > 10) and (int(str(nmbr1)[1:3]) < 20):
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TEENS[nmbr1 % 10]
    else:
        f_part = HUNDREDS[nmbr1 // 100] + ' ' + TENS[(nmbr1 % 100) // 10] + ' ' + ONES[nmbr1 % 10]

    nmbr2 = int(str(nmbr)[6:9])
    if (int(str(nmbr2)[1:3]) > 10) and (int(str(nmbr2)[1:3]) < 20):
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TEENS[nmbr2 % 10]
    else:
        s_part = HUNDREDS[nmbr2 // 100] + ' ' + TENS[(nmbr2 % 100) // 10] + ' ' + ONES[nmbr2 % 10]

    print(z_part + million + f_part + thousand + s_part)
