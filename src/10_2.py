'''
https://uneex.org/Python/GeoPython2021/Homework_PairCounter

Ввести строку и вывести сколько различных пар букв (без учёта регистра)
можно в ней найти. Буквы проверять с помощью .isalpha()

Input:
аwба%Ба б7

Output:
3
'''

s = input().lower()
# Количество пар = (Общее число элементов X Общее число элементов — 1) // 2
a = [i for i in set(''.join(s.split())) if i.isalpha()]

print(len(a)*(len(a)-1)//2)
