'''
http://uneex.org/Python/GeoPython2021/Homework_LongRepeat

Написать функцию blah(S, P), которая проверяет, встречается ли в строке
S шаблон P, и возвращает наибольшую длину подстроки, образованной
повторением шаблона P, которая встречается в S. Если шаблон встречается
в строке, но без повторений, возвращается 1, а если и шаблона нет — 0.

Input:
print(blah("Hey blah, blahblahblah, more than blahblah, blah-blah!", "blah"))

Output:
12
'''

def find_string(S,P):
    start = -1
    l = set()
    while True:
        start = S.find(P, start+1)
        if start == -1:
            return sorted(l)
        l.add(start)


def find_max(L, P):
    max_v = 0
    count = 1
    for i in range(len(L)-1):
        if L[i] + len(P) == L[i+1]:
            count += 1
        else:
            if count > max_v:
                max_v = count
            count = 1

    if count > max_v:
        max_v = count
        
    return max_v*len(P)


def blah(S,P):
    if S.count(P)>1:
        return find_max(find_string(S,P), P)
    elif S.count(P) == 1:
        return 1
    else:
        return 0


s = input()
k = input()

print(blah(s,k))
