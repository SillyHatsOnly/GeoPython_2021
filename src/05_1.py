'''
http://uneex.org/Python/GeoPython2021/Homework_Vovels

Ввести строку и посчитать, сколько в ней содержится английских
гласных букв («y» считается гласной!).

Input:

The Quick Brown Fox Jumps Over The Lazy Dog
Output:

12
'''

s = input()
alpha = 'aeiouy'

count = 0
for i in s:
    if i.lower() in alpha:
        count += 1
print(count)
