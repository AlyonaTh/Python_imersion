# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

# text = "C:\Users\tyoaa\OneDrive\Рабочий стол\python_imersion\Sem5\Practical1.py"
# Выдает ошибку при вводе  \Users
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
text = "C:\\Users\\tyoaa\\OneDrive\\Рабочий стол\\python_imersion\\Sem5\\Practical1.py"


def path_file(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension


print(path_file(text))
