'''
https://uneex.org/Python/GeoPython2021/Homework_Screen

Написать четыре функции:

- screen(width, height, space), которая создаёт «текстовый экран» размером
  width×height, при этом «пустыми местами» в нём служат символы space.
  Функция возвращает только что созданный экран.

- show(screen), которая выводит экран screen в виде прямоугольника

- hline(screen, x0, x1, y, ink), которая заменяет в строке y экрана screen
  символы на позиции с x0 по x1-1 на строку ink, т. е. «рисует горизонтальную
  линию»

- vline(screen, x, y0, y1, ink), которая заменяет в столбце x экрана screen
  символы на позиции с y0 по y1-1 на строку ink, т. е. «рисует вертикальную
  линию»

Реализация «экрана» — произвольная. Координаты всегда упорядочены,
т. е. x0 ⩽ x1 и y0⩽y1, и не выходят за границы экрана.

Input:
S = screen(15, 7, '.')
vline(S, 3, 2, 6, '|')
hline(S, 2, 13, 3, '-')
show(S)

Output:
...............
...............
...|...........
..-----------..
...|...........
...|...........
...............
'''

def screen(width, height, space):
    return [space*width]*height


def hline(screen, x0, x1, y, ink):
    S[y] = S[y][:x0] + ink*(x1-x0) + S[y][x1:]
    

def vline(screen, x, y0, y1, ink):
    for i in range(y0, y1):
        S[i] = S[i][:x] + ink + S[i][x+1:]

def show(screen):
    for i in screen:
        print(i)

S = screen(15,7, '.')
vline(S, 3, 2, 6, '|')
hline(S, 2, 13, 3, '-')
show(S)
