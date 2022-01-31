'''
http://uneex.org/Python/GeoPython2021/Homework_CalcDiscr

Ввести a, b, c и x, по одному вещественному числу в строке, и вывести
результат подстановки значений в уравнение ax2+bx+c

Input:
1
2.2
3
4

Output:
27.8
'''

a = float(input())
b = float(input())
c = float(input())
x = float(input())

print(a*x**2 + b*x + c)
