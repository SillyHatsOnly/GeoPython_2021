'''
http://uneex.org/Python/GeoPython2021/Homework_ConfFormula

Ввести в столбик три вещественных числа x, y и z. Вычислить формулу:

(max(x,y,z)**2 - 2**x * min(x,y,x)) / (sin(2*x) + max(x,y,z)/min(x,y,z))

Проверить возможное деление на 0 и вместо ответа вывести 0, если оно
предвидится. В противном случае вывести результат вычислений.

Последовательностями python и функциями min() и max() пользоваться
нельзя!

С помощью тернарной операции и операции «:=» выбор минимального
из трёх чисел записать несложно.

Input:
2
3
4

Output:
6.435019351154122
'''

from math import sin

#(max(x,y,z)**2 - 2**x * min(x,y,x)) / (sin(2*x) + max(x,y,z)/min(x,y,z))

x = float(input())
y = float(input())
z = float(input())

new_max = M if (M := x if x > y else y) > z else z
new_min = N if (N := x if x < y else y) < z else z

if new_min == 0:
    print(0)
else:
    up = new_max**2 - 2*x*new_min
    down = sin(2*x) + new_max/new_min
    if down != 0:
        print(up/down)
    else:
        print(0)
