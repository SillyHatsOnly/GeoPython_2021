'''
https://uneex.org/Python/GeoPython2021/Homework_BinSearch

Написать функцию, binsearch(x, A), реализующую двоичный поиск элемента x
по индексируемой последовательности (списку, кортежу или даже range) A.

Гарантировано, что последовательность упорядочена по возрастанию.

Функция возвращает True, если x∈A и False в противном случае.

Input:
print(binsearch(123, sorted([123, 12, 45, 67, 23, 678, 12345, 4, 23, 768])))

Output:
True
'''

def binsearch(x, A):
    while True:
        i = len(A)//2
        l_p = A[:i]
        r_p = A[i:]
        if x < A[i]:
            A = A[:i]
        elif x > A[i]:
            A = A[i:]
        elif x == A[i]:
            return True
        else:
            return False

x = int(input())
A = list(map(int, input().split(', ')))

print(binsearch(x, sorted(A)))
