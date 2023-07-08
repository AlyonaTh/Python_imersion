# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def fun_uni(text: str):
    return sorted(list(map(ord, set(text))), reverse=True)


data_ = input("Print text: ")
print(*fun_uni(data_))