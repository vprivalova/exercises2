"""
Задание 13.
Дима часто пользуется общественным транспортом и всегда проверяет номер билета,
является ли он "счастливым". Счастливым считается билет, имеющий в номере четное
количество цифр. Причем,  сумма цифр первой половины номера равна сумме цифр
второй половины.  Программа на вход получает  последовательность номеров билетов.
Ввод номеров должен завершить тогда, когда будет введен "счастливый" билет.
Программа должна вывести его порядковый номер. Счет начинается с 1.
"""

luck = 0
half1 = 0
half2 = 0
cnt = 1

ticket = input()

while luck == 0:
    if len(ticket) % 2 == 0:
        for index1 in range(len(ticket) // 2):
            half1 = half1 + int(ticket[index1])

        for index2 in range(len(ticket) // 2, len(ticket)):
            half2 = half2 + int(ticket[index2])

        if half1 == half2:
            print(cnt)
            luck = luck + 1
            break
        else:
            ticket = input()
    else:
        ticket = input()
    cnt = cnt + 1
    half1 = 0
    half2 = 0
