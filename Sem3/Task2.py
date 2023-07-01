# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в верхнем регистре в остальных случаях

data = input('Input data: ')

if data.isdigit():
    data = int(data)
elif data.replace('.','').replace('-','').isdigit()\
        and data.count('.') == 1 and\
        data.count('-') <= 1 and (data.startswith('-') and data.count('-') == 1 or data.count('-') == 0):
    data = float(data)
elif data != data.lower():
    data = data.lower()
else:
    data = data.upper()

print(type(data), data)