'''
https://uneex.org/Python/GeoPython2021/Homework_Matrix

Ввести квадратную «матрицу» — последовательность строк, содержащих целые числа,
разделённые пробелами.

Вывести номер столбца, сумма элементов в котором наибольшая.

Если таких столбцов несколько, вывести самый маленький номер.

Input:
12 34 56 78 90
23 45 67 89  2
23 65 90 12 45
13  4 35 46 57
80 79 68 57 46

Output:
2
'''

l = [list(map(int, input().split()))]
while True:
    if len(l) == len(l[0]):
        break
    l.append(list(map(int, input().split())))

max_v = 0
row = 0
for i in range(len(l)):
    temp = 0
    for j in range(len(l)):
        temp += l[j][i]

    if temp > max_v:
        max_v = temp
        row = i
    elif temp == max_v:
        if i < row:
            row = i

print(row)
