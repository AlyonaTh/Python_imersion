# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.
data = (1, 2.5, 'dare', [5.5, 5], True, 34, False)
res = dict()
for values in data:
    # res.setdefault(type(values), values)
    key = type(values)
    if key not in res:
        res[key] = []
    res[key].append(values)
print(res)