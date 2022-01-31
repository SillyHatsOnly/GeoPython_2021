'''
http://uneex.org/Python/GeoPython2021/Homework_Theodor

Робот Фёдор посылает с космической станции зашифрованные сообщения,
в которых читать надо каждую N-ю букву.

Ввести две строки — зашифрованное сообщение (с лишними буквами),
и слово, которое заведомо присутствует где-то в исходном сообщении.

Вывести самую длинную из подходящих расшифровок.

Если слово не встречается в шифровке, вывести "<NO>".

Vikingsed xeric sortrsebony capel  teakungetUginesheemolleeq criteriumoud
antisel
'''


def search_first_indexes(s,k):
    start = -1
    l = []
    while True:
        start = s.find(k[0], start+1)
        if start == -1:
            break
        l.append(start)
    return l


def search_word(s, k, start, step):
    for i in range(1, len(k)):
        if start+step < len(s) and k[i] == s[start+step]:
            start = start + step
        else:
            return '<NO>'
    return step


def theodor(string, key):

    if string.find(key[0]) == -1:
        return '<NO>'

    max_step = (len(string)-1) // (len(key)-1)
    ilist = search_first_indexes(string,key)

    answr = []
    for i, start in enumerate(ilist):
        temp = [(start, step) for step in range(1, max_step+1)
                if search_word(string,key,start,step) !='<NO>']
        if len(temp)!= 0:
            answr.extend(temp)

    if len(answr) == 0:
        return '<NO>'

    max_len = ''
    for arr in answr:
        start,step = arr
        if start-step > 0:
            new_string = string[start-step:0:-step][::-1] + string[start::step]
        else:
            new_string = string[start::step]

        if len(new_string) > len(max_len):
            max_len = new_string

    return max_len
    

s = input()
k = input()
print(theodor(s,k))
