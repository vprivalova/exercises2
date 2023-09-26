"""
Задание 5.
Даны три строки. Выведите на экран только те символы, которые есть лишь в одной из этих трёх строк.
"""

line1 = input()
line2 = input()
line3 = input()

smbl_lines_srtd = ''
result = []
cnt = 0

lines = line1 + line2 + line3
smbl_lines = list(lines)


for item in smbl_lines:
    if item not in smbl_lines_srtd:
        smbl_lines_srtd = smbl_lines_srtd + item

smbl_lines_srtd = sorted(smbl_lines_srtd)


for elem in smbl_lines_srtd:
    for item in smbl_lines:
        if item == elem:
            cnt = cnt + 1
    if cnt == 1:
        result.append(elem)
    cnt = 0

print(*result)
