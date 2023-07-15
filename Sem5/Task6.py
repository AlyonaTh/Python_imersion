# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

# my_gen = (f'\n' if j == 10 else f' {j}*{i}={i * j:3d} ' for i in range(2, 10) for j in range(2, 11))
# my_gen_1 = (f'\n' if j == 6 else f' {j}*{i}={i * j:3d} ' for i in range(2, 10) for j in range(2, 7))
# my_gen_2 = (f'\n' if j == 10 else f' {j}*{i}={i * j:3d} ' for i in range(2, 10) for j in range(6, 11))
# print(*my_gen)
# print(*my_gen_1)
# print(*my_gen_2)

res = ''
for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i + 4):
            if k != i + 4 - 1:
                res += f'{k} * {j} = {j * k}\t'
            elif j != 10:
                res += f'{k} * {j} = {j * k}\n'
            else:
                res += f'{k} * {j} = {j * k}\n\n'

print(res)

gen_tab = (f'{k:>2} * {j:>2} = {j * k:>2}\t' if k != i + 4 - 1 else f'{k:>2} * {j:>2} = {j * k:>2}\n' if j != 10 \
    else f'{k:>2} * {j:>2} = {j * k:>2}\n\n' for i in range(2, 10, 4) for j in range(2, 11) for k in range(i, i + 4))
print(*gen_tab)
