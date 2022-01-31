'''
http://uneex.org/Python/GeoPython2021/Homework_MultTable

Ввести два натуральных числа, M и N. Вывести таблицу умножения от 1×1 до M*N
в приведённом ниже формате (по колонкам, но без учёта количества разрядов в
числе).

Input:

4
5

Output:

1 * 1 = 1; 2 * 1 = 2; 3 * 1 = 3; 4 * 1 = 4; 5 * 1 = 5
1 * 2 = 2; 2 * 2 = 4; 3 * 2 = 6; 4 * 2 = 8; 5 * 2 = 10
1 * 3 = 3; 2 * 3 = 6; 3 * 3 = 9; 4 * 3 = 12; 5 * 3 = 15
1 * 4 = 4; 2 * 4 = 8; 3 * 4 = 12; 4 * 4 = 16; 5 * 4 = 20
'''

N,M = int(input()), int(input())
N,M = min(N,M), max(N,M)

lst=[]
for i in range(1, N+1):
    s = ''
    for j in range(1, M+1):
        s += str(j) + ' * ' + str(i) + ' = ' + str(i*j) + '; '
    lst.append(s)

for i in lst:
    print(i)
