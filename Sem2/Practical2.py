# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
import math

def add(a,b,c,d):
    sum_up = a * d + c * b
    sum_down = b * d
    x = Fraction(a/b)
    y = Fraction(c/d)
    return f'{sum_up}/{sum_down} = {sum_up/sum_down} | {x+y}'
def mul(a,b,c,d):
    sum_up = a * c
    sum_down = b * d
    x = Fraction(a/b)
    y = Fraction(c/d)
    return f'{sum_up}/{sum_down} = {sum_up/sum_down} | {x*y}'


first_fr = input('Print a/b: ')
second_fr = input('Print c/d: ')
a, b = first_fr.split(sep="/")
c, d = second_fr.split(sep="/")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print(f'addition is {add(a,b,c,d)}')
print(f'multiplication is {mul(a,b,c,d)}')
