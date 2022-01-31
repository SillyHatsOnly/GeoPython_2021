'''
http://uneex.org/Python/GeoPython2021/Homework_TkinterSum

Пользуясь статьёй про Tkinter, написать простейшее приложение (программу),
в котором будет:

- два поля ввода A1 и A2 типа tkinter.Entry

- одно текстовое поле L типа tkinter.Label

- одна кнопка B типа tkinter.Button

При нажатии кнопки в текстовом поле должна появляться сумма чисел,
находящихся в полях ввода.

Если хотя бы одна из строк в полях ввода не является числом, содержимое L
не меняется.

С самого начала поля ввода пусты, а в L записана строка "0".

Условие: функция, которая считывает значения из A, проверяет их правильность
и записывает результат в L, должна быть зарегистрирована при создании
кнопки B как её свойство command.

Внимание!. Программа должна использовать оператор import tkinter, как в
примере из лекции, (а не from tkinter import *, как в статье).

Input:
23 и 456 в полях ввода A1 и A2

Output:
479 в поле вывода L

*Обратите также внимание на то, что тестированием такой программы (она
ничего не вводит со стандартного ввода и ничего не выводит на стандартный
вывод) занимается специальный робот. Робот тупой — мы с вами куда хитрее,
так что если тесты не проходят, сигнальте мне: возможно, вы просто его
перехитрили
'''

import tkinter

window = tkinter.Tk()
window.title('Сумматор')
window.geometry('450x200')

# поле ввода
A1=tkinter.Entry(window, width=25,) #state='disabled')
A1.grid(column=0,row=1)

A2=tkinter.Entry(window, width=25,) #state='disabled')
A2.grid(column=2,row=1)

# текст в окне
L = tkinter.Label(window, text='0')
L.grid(column=1, row=0)

def clicked():
    a_1 = A1.get()
    a_2 = A2.get()
    if a_1.isdigit() and a_2.isdigit():
        L.configure(text=int(a_1) + int(a_2))

# кнопка
B = tkinter.Button(window, text='Click', command=clicked, bg='red', fg='white')
B.grid(column=1, row=1)

window.mainloop()
