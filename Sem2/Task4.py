# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import decimal
import math

LEN_DIG = 42
D = 1000
PI = decimal.Decimal(math.pi)
decimal.getcontext().prec = LEN_DIG
diameter = decimal.Decimal(input("Print diameter: "))
if diameter < D:
    len_circle = PI * diameter
    area_circle = PI * diameter ** 2 / 4
    print(f'{len_circle =}')
    print(f'{area_circle =}')
else: print('Again')