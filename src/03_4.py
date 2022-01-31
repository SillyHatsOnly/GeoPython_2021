'''
http://uneex.org/Python/GeoPython2021/Homework_CorrectDate

Ввести в столбик три целых заведомо положительных числа — номер года,
номер месяца и номер дня в месяце. Проверить, есть ли такой день в
месяце, и если да, выдать "YES", а если нет — "NO". Считать високосными
все кратные 4 номера годов.

Input:
2019
2
29

Output:
NO
'''

year = int(input())
month = int(input())
day = int(input())

high_year = [31,29,31,30,31,30,31,31,30,31,30,31]
low_year = [31,28,31,30,31,30,31,31,30,31,30,31]

if day > 31 or day < 1 or month > 12 or month < 1:
    print('<NO>')
else:
    if year%4 == 0 and day in range(high_year[month-1]+1) or year%4 != 0 and day in range(low_year[month-1]+1):
        print('YES')
    else:
        print('NO')
