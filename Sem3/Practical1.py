# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

data = [1, 2.5, 1, 'dare', True, 34, False, True]
res = list(set(data))
print(res)

res = []
for i in data:
    if i not in res:
        res.append(i)
print(res)