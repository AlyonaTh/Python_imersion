# Напишите функцию для транспонирования матрицы


def trans_matrix(a: list) -> list:
    # return map(list, zip(*a))
    return [list(x) for x in zip(*a)]


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(trans_matrix(a))