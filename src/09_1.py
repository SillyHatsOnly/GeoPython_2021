'''
https://uneex.org/Python/GeoPython2021/Homework_BackBack

Ввести строку, содержащую пары натуральных чисел.

Числа в парах разделены двоеточием.

Строка начинается и заканчивается на некоторый один и тот же символ
(не цифра, но в разных случаях он может быть разным), и этот же символ
стоит между парами.

Вывести эти числа в обратном порядке через пробел.

Input:
-12:3-4:56-7:8-9:10-

Output:
10 9 8 7 56 4 3 12
'''

##s = input()
##symbol = s[0]
##a = s.strip(symbol).split(symbol)
##
##l = []
##for i in a:
##    a,b = i.split(':')
##    l.append(a)
##    l.append(b)
##
##print(*l[::-1])


s = input()
symbol = s[0]

l = []
for i in s.strip(symbol).split(symbol):
    l.extend(i.split(':'))

print(*l[::-1])
