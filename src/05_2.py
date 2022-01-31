'''
http://uneex.org/Python/GeoPython2021/Homework_Braces

Вводится арифметическое выражение, содержащее круглые скобки
(в действительности вводится что угодно, содержащее круглые скобки,
но это неважно ☺). Проверить, правильно ли с точки зрения арифметики
расставлены эти скобки.

Скобки считаются расставленными правильно, если после каждой открывающей
скобки можно найти однозначно соответствующую ей закрывающую. Больше
ничего проверять не надо.

Вывести "YES", если скобки расставлены правильно, и "NO" в противном случае.

Input:
12+(13/14+((15/16))-17*18+(19/20))

Output:
YES
'''

s = input()

r = s.count('(')
l = s.count(')')

if l == r:
    print('YES')
else:
    print('NO')
