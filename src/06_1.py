'''
http://uneex.org/Python/GeoPython2021/Homework_DummyFunction

Это примитивная задача типа «написать функцию». Она нужна для того,
чтобы освоить такой тип задач. Написать функцию divides(a, b), которая
для целых a и b возвращает целый результат деления a на b, если a
делится на b, или же деления b на a, если b делится на a, или 0 в
противном случае. На 0, понятно, ничего не делится.

Input:
print(divides(1000,10), divides(64, 32768), divides(1024, 12345))

Output:
100 512 0
'''

def divides(a,b):
    if a == 0 and b == 0:
        return 0
    elif a%b == 0:
        return a//b
    elif b%a == 0:
        return b//a
    else:
        return 0

a = int(input())
b = int(input())

print(divides(a,b))
