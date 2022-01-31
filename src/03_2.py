'''
http://uneex.org/Python/GeoPython2021/Homework_SquareEquation

Ввести в столбик три вещественных числа: a, b и c, вывести все
вещественные решения уравнения ax2+bx+c=0. При a≠0 это уравнение
превращается в квадратное. Решения выводить через пробел в
порядке возрастания, если решений нет, вывести 0, если их
бесконечно много — -1.

Input:
1
-3
2

Output:
1.0 2.0
'''


a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print(-1)
elif a == 0 and b == 0 and c != 0:
    print(0)
elif a == 0:
    print(-c/b)
else:
    d = b**2 - 4*a*c
    if d >0:
        l = [(-b + d**0.5)/a*c, (-b - d**0.5)/a*c]
        print(min(l), max(l))
    elif d == 0:
        print(-b/(2*a))
    else:
        print(0)
