#  Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX = 16
NINE = 9
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15

def Trans(mod, number: int) -> str:
    res: str = ''
    while number:
        if number % mod < NINE:
            res = str(number % mod) + res
            number //= mod
        else:
            num = number % mod
            if num == A:
                res = "A" + res
            elif num == B:
                res = "B" + res
            elif num == C:
                res = "C" + res
            elif num == D:
                res = "D" + res
            elif num == E:
                res = "E" + res
            elif num == F:
                res = "F" + res
            number //= mod
    return res


num = int(input('Print number: '))
print(hex(num))
print(Trans(HEX, num))