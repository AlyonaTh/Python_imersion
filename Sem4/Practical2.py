#  Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def fun(**kwargs) -> dict:
    res = dict()
    for key, value in kwargs.items():
        res[value] = key
    return res


print(fun(rew=4, trj=5, vois=45, фыгя='wvahf',))