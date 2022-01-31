'''
http://uneex.org/Python/GeoPython2021/Homework_CalcTrigonometry

Ввести x, вычислить формулу и вывести результат:

x*log(x)-1/(12*x**2 + 17*sin(x) + 5)

Input:
1.234

Output:
0.23402832649377744
'''

from math import log, sin

x = float(input())

print(x*log(x) - 1/(12*x**2 + 17*sin(x) + 5))

