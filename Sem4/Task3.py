# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def m_dict(text: str) -> dict[str, int]:
    mdict = dict()
    li = list(map(int, text.split()))
    for i in range(min(li), max(li)):
        mdict.setdefault(chr(i), i)
    return mdict


data = input("Input twu number: ")
print(m_dict(data))
