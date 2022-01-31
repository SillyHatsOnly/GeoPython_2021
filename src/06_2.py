'''
http://uneex.org/Python/GeoPython2021/Homework_ArsakSequence

(Ж. Арсак) Написать функцию seq(n), которая последовательно вычисляет
значения последовательности {Pi} для натурального n по формуле ниже,
до тех пор, пока очередной член этой последовательности не станет
равен 1, и возвращает наибольший элемент такой последовательности.

Формула:
0. P0=n
1. P(i+1) = Pi/2, если Pi чётно
2. P(i+1)=3Pi + 1, если Pi нечётно

Input:
print(seq(27), seq(1), seq(16), seq(101))

Output:
9232 1 16 304
'''

def seq(n):
    if n < 1:
        return 'Error'
    P = n
    vmax = P
    while P != 1:
        if P%2 == 0:
            P = P//2
        else:
            P = 3*P + 1

        if P > vmax:
            vmax = P

    return vmax


n = int(input())
print(seq(n))
