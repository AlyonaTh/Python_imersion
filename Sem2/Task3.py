#  Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BIN = 2
OCT = 8


def Trans(mod, number: int) -> str:
    res: str = ''
    while number:
        res = str(number % mod) + res
        number //= mod
    return res


num = int(input('Print number: '))
print(bin(num))
print(Trans(BIN, num))
print(oct(num))
print(Trans(OCT, num))
