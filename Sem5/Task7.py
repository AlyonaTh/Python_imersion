# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def gen_easy(n: int):
    count = 2
    while count <= n:
        for j in range(2, count):
            if count % j == 0:
                break
        else:
            yield count
        count += 1


# gen_easy(int(input('Input number: ')))

for num in gen_easy(int(input('Input number: '))):
    print(num)
