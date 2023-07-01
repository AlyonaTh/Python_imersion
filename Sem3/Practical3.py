# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

baggage = {'matches': 1, 'cup': 2, 'tent': 10, 'ration': 5, 'spare shoes': 3}
capacity = int(input('Input capacity: '))

packaging_option = []
summary = []
for key, value in baggage.items():
    if value <= capacity:
        capacity -= value
        packaging_option.append(key)
print(packaging_option)
