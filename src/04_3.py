'''
http://uneex.org/Python/GeoPython2021/Homework_MinSin

Ввести в столбик 2*N целых чисел, не равных нулю. Назовём меньшее число
в очередной введённой паре A, а большее — B. Для чисел A, A+1, …, B-1,
B выбирается такое, значение синуса на котором минимально. Вывести N таких
чисел. A может быть больше, меньше или равно B (в последнем случае в наборе
всего одно это число). Ввод заканчивается двумя нулями.

Input:
1
10
25
9
-200
300
1000
-25
0
0

Output:
5
11
11
344
'''
from math import sin

def min_sin():
    lst = []
    while True:
        A = int(input())
        B = int(input())
        if A == 0 and B == 0:
            if len(lst) == 0:
                return 'Error'
            break
        lst.append([min(A,B), max(A,B)])

    answr=[]
    for r in lst:
        min_sin = 2
        index = 0
        start, end = r
        if end == start:
            end += 1
        for i in range(start, end):
            if sin(i) < min_sin:
                min_sin = sin(i)
                index = i
        answr.append(index)

    return answr

print(min_sin())


