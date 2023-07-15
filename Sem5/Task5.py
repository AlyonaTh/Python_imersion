# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)

gen_fb = ("FizzBuzz" if i % 15 == 0 else 'Buzz' if i % 5 == 0 else 'Fizz' if i % 3 == 0 else i for i in range(1, 101))
print(*gen_fb)