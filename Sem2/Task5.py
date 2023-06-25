#  Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

print('a *x^2 + b*x + c = 0')
num_a = float(input('Print number a: '))
num_b = float(input('Print number b: '))
num_c = float(input('Print number c: '))

d = num_b ** 2 - 4 * num_a * num_c
if d > 0 :
    x1 = (-num_b + d ** 0.5)/(2 * num_a)
    x2 = (-num_b - d ** 0.5)/(2 * num_a)
elif d == 0:
    x1 = x2 = -num_b/(2 * num_a)
else:
    d = complex(d, 0)
    x1 = (-num_b + d ** 0.5) / (2 * num_a)
    x2 = (-num_b - d ** 0.5) / (2 * num_a)
print(f'x1 = {x1}, x2 = {x2}')