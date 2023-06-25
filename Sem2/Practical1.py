#  Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX = 16


def Trans(mod, number: int) -> str:
    res: str = ''
    while number:
        res = str(number % mod) + res
        number //= mod
    return res


num = int(input('Print number: '))
print(hex(num))
print(Trans(HEX, num))