# Задание 8
__all__ = ['func', 'puzzle', 'puzzle_dict', 'show_result', 'calendar']

from sys import argv

# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

from math import sqrt as sq
from math import sin as si
from math import cos as co

# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
from random import randint


def func(min_val=1, max_val=10, tries=3):
    num = randint(min_val, max_val)
    while tries:
        number = int(input('Input number: '))
        if number == num:
            return True
        elif number < num:
            print('More')
        else:
            print('Less')
        tries -= 1
    return False


# Задача 4
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def puzzle(puzle_text: str, solutions: list[str], tries: int) -> int:
    print(puzle_text)
    solutions = list(map(lambda x: x.lower(), solutions))
    num = 0
    while num < tries:
        user_input = input("Answer number: ").lower()
        if user_input in solutions:
            print(f'This is the {num + 1} try')
            return num + 1
        else:
            print('Try again')
        num += 1
    print('Lose')
    return 0
# Задание 5
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

_dict_res = {}
def puzzle_dict():
    dict_puzzle = {'What is blue?': ['sea', 'sky', 'bird'], 'What is green?': ['tree', 'card', 'leaf'],\
                   'What has four legs, but can’t walk?': ['table', 'chair', 'lazy body']}

    for key, values in dict_puzzle.items():
        tries = int(input('Enter number of tries: '))
        _dict_res[key] = puzzle(key, values, tries)

#Задание 6
#Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
#Функция формирует словарь с информацией о результатах отгадывания.
#Для хранения используйте защищённый словарь уровня модуля.
#Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
#Для формирования результатов используйте генераторное выражение.


def show_result():
    for key, value in _dict_res.items():
        print(key, ' the try is ', value)


#Задание 7
#Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
#Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
#Для простоты договоримся, что год может быть в диапазоне [1, 9999].
#Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
#Проверку года на високосность вынести в отдельную защищённую функцию.

def calendar(date: str):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif 1 <= day <= 28 + _leap_year(year):
            return True
        else:
            return False
    return False


def _leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def calend_tetminal():
    date = argv[1]
    print(calend(date))