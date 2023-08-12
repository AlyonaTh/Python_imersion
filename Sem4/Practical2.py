#  Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def fun(**kwargs) -> dict:
    res = dict()
    for key, value in kwargs.items():
        if not value.__hash__:
            res[str(value)]=key
        else:
            res[value] = key
    return res


print(fun(rew=4, trj=5, vois=[1,4,5], фыгя='wvahf',))