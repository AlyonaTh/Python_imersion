# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

G_YEAR = 1582
CENTURE = 100
DIV_YEAR = 4

def vis_year(year: int):
    if year > G_YEAR:
        if (year%DIV_YEAR==0 or year%(DIV_YEAR*CENTURE)==0) and year%CENTURE != 0:
            print('Это високосный год')
        else: print('Это невисокосный год')
    else: print('Не по Григорианскому календарю')
year = int(input('Введите год: '))
vis_year(year)