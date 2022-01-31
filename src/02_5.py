'''
http://uneex.org/Python/GeoPython2021/Homework_AthomizeFormula

Ввести переменную x, вычислить формулу, и вывести результат.

Обязательное условие: на каждую операцию связывания ("=") должно
приходиться не более одной арифметической операции или один вызов
функции (см пример в лекции)

|x2-x3|- 7x/(x3-15x)

Input:
-1.23

Output:
3.8927814656746076
'''

x = float(input())

x2 = x**2
x3 = x**3
x7 = 7*x
x15 = 15*x
div = x3-x15
div2 = x2-x3
mod = abs(div2)
dec = x7/div
answr = mod-dec

print(answr)
