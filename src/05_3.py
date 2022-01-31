'''
http://uneex.org/Python/GeoPython2021/Homework_Caesar

Вводится строка — предложение, написанное латинскими буквами (большими
и маленькими). Предложение зашифровано шифром цезаря. Известно, что
исходное сообщение обязательно заканчивается словами «Ave Caesar!».
Строчные буквы в сообщении заменяются на строчные, прописные — на
прописные. Используется стандартный английский алфавит. Расшифровать и
вывести это сообщение.

Input:
Ej pda bwya kb wixecqepu, nabqoa pda pailpwpekj pk cqaoo. Wra Ywaown!

Output:
In the face of ambiguity, refuse the temptation to guess. Ave Caesar!
'''
#version 1.0
def caesar(s):
    if len(s) < len('Ave Caesar!'):
        return 'Error'
    alp = 'abcdefghijklmnopqrstuvwxyz'
    gap = ord('r') - ord(s[-2])
    new_s = ''
    for i in s:
        if ord(i) < 65 or ord(i) > 122:
            new_s += i
            continue
 
        f = alp.find(i.lower()) + gap
        if f > len(alp) - 1:
            f = f - len(alp)
        elif f < 0:
            f = f + len(alp)
        new_i = alp[f]
        
        if i.isupper():
            new_s += new_i.upper()
        else:
            new_s += new_i.lower()
    return new_s

#version 2.0
def shift(alpha, letter, offset):
    lower = False
    if letter.islower():
        letter = letter.upper()
        lower = True
    if letter not in alpha:
        return letter
    cidx = alpha.index(letter)
    nidx = (cidx + offset) % len(alpha)
    nletter = alpha[nidx]
    if lower:
        nletter = nletter.lower()
    return nletter

def shiftall(alpha, string, offset):
    return ''.join(shift(alpha, c, offset) for c in string)
    
def caesar(s):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # guess the offset
    for i in range(len(alpha)):
        test = 'Ave Caesar!'
        if shiftall(alpha, s[-len(test):], i) == test:
            break
    else:
        raise Exception('unknown offset')
    # if you exit from 'for-loop' by 'break', you still have
    # the correct 'i' value stored, soooo...
    # decypher
    return shiftall(alpha, s, i)


s = input()
print(caesar(s))
