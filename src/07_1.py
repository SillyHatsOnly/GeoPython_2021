'''
https://uneex.org/Python/GeoPython2021/Homework_PosCount

Вводятся построчно последовательности чисел через запятую. Если в
строке нет запятых — это конец ввода, она не учитывается. Вывести
общее количество положительных чисел.

Input:
1, 3, -3, 0, 234, 657
-2, -4356, -345, 0, -11, -2134123412341234, 0, 0
777, 2
how boring!

Output:
6
'''
count = 0
while True:
    s = input()
    symbol = ','
    if symbol not in s:
        print(count)
        break
    #l = [int(i) > 0 for i in s.split(symbol) if symbol in s]
    l = [i > 0 for i in list(map(int, s.split(symbol))) if symbol in s]
    count += l.count(True)
