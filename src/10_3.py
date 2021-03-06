'''
https://uneex.org/Python/GeoPython2021/Homework_PublicFriend

Вводятся в столбик пары натуральных чисел через запятую. Каждая пара M, N
обозначает взаимное знакомство людей под номерами M и N. Ввод заканчивается
парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с
человеком N ;) ).

Вывести через пробел в порядке возрастания номера тех,
кто знаком со всеми остальными, или пустую строку, если таких нет.

Input:
7, 9
1, 7
9, 2
9, 2
9, 7
2, 9
9, 2
2, 9
7, 1
9, 2
9, 2
2, 1
7, 2
7, 9
7, 1
7, 1
0, 0

Output:
2 7
'''
d = {}
while True:
    k,v = list(map(int, input().split(', ')))
    if [k,v] == [0,0]:
        break
    
    if k in d:
        d[k].add(v)
    else:
        d[k] = {v}

    if v in d:
        d[v].add(k)
    else:
        d[v] = {k}

l = []
for i in d:
    if len(d[i]) == len(d)-1:
        l.append(i)

print(*sorted(l))
