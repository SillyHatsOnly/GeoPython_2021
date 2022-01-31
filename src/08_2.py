'''
https://uneex.org/Python/GeoPython2021/Homework_Cross

Написать функцию cross(width, paper, ink), которая на вход принимает
три параметра:
- натуральное число width⩾2
- две строки единичной длины: paper и ink

Возвращать эта функция должна строковый объект, при выводе на экран
которого получается приведенная ниже фигура.

Это квадрат шириной width, стороны и диагонали которого состоят из
строки ink, а остальное пространство заполнено строкой paper.

Input:
print(cross(11, ".", "*"))

Output:
***********
**.......**
*.*.....*.*
*..*...*..*
*...*.*...*
*....*....*
*...*.*...*
*..*...*..*
*.*.....*.*
**.......**
***********
'''

def cross(width, paper, ink):
    s = ink*width
    for i in range(1, width-1):
        s += '\n' + ink
        for j in range(1, width-1):
            if j == i or j == width-1 - i:
                s += ink
            else:
                s += paper
        s += ink
    s += '\n' + ink*width
    return s

w = int(input('Введите число больше 2: '))
p = input('Введите символ фона: ')
i = input('Введите символ чернила: ')

print(cross(w, p, i))
