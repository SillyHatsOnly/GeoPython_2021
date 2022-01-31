'''
https://uneex.org/Python/GeoPython2021/Homework_NumSearch

В первой строке вводится несколько (более одного) чисел через запятую.
В последующих строках — произвольный текст. Последняя строка содержит
одну точку, это конец ввода.

Вывести, сколько раз каждое из этих чисел встречается в тексте.

Достаточно воспользоваться строковым методом .count() и подсчитать
количество вхождений числа как подстроки;

не нужно учитывать, что одно число может встречаться внутри другого,
внутри слова и т. п.

Input:
123, 2, 777, -8, 2, 100500
1w21e23qr123rwe34rt5t5
это кот на клавиатуру 8 раз сел и 22 клавиши нажал!
777777 7777
12-8=-123, ой, ошибся…
.

Output:
123: 2
2: 7
777: 3
-8: 1
2: 7
100500: 0
'''

k = input().split(', ')
l = {}
while True:
    s = input()
    if s is '.':
        print(l)
        break
    for i in k:
        l.update({i: s.count(i)})
