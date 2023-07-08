# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def company(lst_cop: dict[str, list[int]]) -> bool:
    res = dict()
    for key, value in lst_cop:
        res[key] = sum(value)
        if sum(value) < 0:
            return False
    print(res)
    return True


lst_cop = {'Cola': [10, -20, 15], 'Google': [50, -60, 70], 'Microsoft': [-50, -10, 20]}
print(company(lst_cop))