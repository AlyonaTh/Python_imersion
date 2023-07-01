# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.

my_list = [1, 2, 8, 9, 4, 4, 8, 2, 5, 8, 1]

print(list(set(my_list)))

new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)