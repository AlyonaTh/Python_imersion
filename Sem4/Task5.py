# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.


def money_us(names: list[str], salaries: list[int], procent) -> dict | None:
    if len(names) != len(salaries) != len(procent):
        return None
    prem = list(map(lambda x: float(x.replace('%', '')), procent))
    res = {}
    for i in range(len(names)):
        res[names[i]] = salaries[i] * prem[i]/100
    return res


names = ['Alex', 'Max', 'Bob']
salaries = [1000,  1200, 1500]
procent = ['15%', '20%', '50%']
print(money_us(names, salaries, procent))