# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


text = 'thrjwoujrknn ejroiwj kwjwojrwlrjwli uwo'
m_dict = {i: ord(i) for i in text}
print(m_dict)