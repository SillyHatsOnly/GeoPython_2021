'''
https://uneex.org/Python/GeoPython2021/Homework_MostPopular

Ввести строку, состоящую из разделённых пробелами последовательностей
маленьких и больших латинских букв. Вывести, сколько различных слов
(без учёта регистра) встречается в этой строке чаще всего.

Input:
dAh Dit dah dIT dAH Dit GIgly diGLy biglY GiGly bOOm quack OH quack

Output:
2
'''

s = input().lower().split()
d = {}
for i in s:
    d[i] = s.count(i)

m = 0
for i in d.values():
    if i == max(d.values()):
        m +=1
print(m)
