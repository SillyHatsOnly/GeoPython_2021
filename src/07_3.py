'''
https://uneex.org/Python/GeoPython2021/Homework_ThirdsOut

Написать функцию squeeze(), которая получает на вход числовой список,
обрабатывает его, удаляя элементы, которые являются суммой предыдущего
и последующего элементов, и возвращает результат.

Input:
print(squeeze([1, 5, 4, 3, 7, 6, 14, 8, 2]))

Output:
[1, 4, 3, 7, 6, 8, 2]
'''

def squeeze(l):
    new_l = [l[0]]
    for i in range(1, len(l)):
        try:
            if not l[i] == l[i-1] + l[i+1]:
                new_l.append(l[i])
        except IndexError:
            new_l.append(l[i])
    return new_l


l = list(map(int, input().split(', ')))

print(squeeze(l))
