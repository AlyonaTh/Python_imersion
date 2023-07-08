# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_ind(lsr: list[int], ind_1: int, ind_2: int) -> int:
    min_ind = 0
    max_ind = len(lsr)
    min_ = min(ind_1, ind_2)
    max_ = max(ind_1, ind_2)
    if min_ >= min_ind:
        min_ind = min_
    if max_ <= len(lsr):
        max_ind = max_
    return sum(lsr[min_ind:max_ind])


list_t = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(sum_ind(list_t, 5, 4))
