'''
http://uneex.org/Python/GeoPython2021/Homework_TriangleCheck

Ввести в столбик три положительных вещественных числа (проверять
правильность не надо), и вывести YES, если из отрезков указанной
длины можно сложить треугольник, и NO в противном случае.

Input:
3
4
5

Output:
YES
'''

a = int(input())
b = int(input())
c = int(input())

if a+b < c and a+c < b and c+b < a:
    print('NO')
else:
    print('YES')
