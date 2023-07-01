# Три друга взяли вещи в поход. Сформируйте словарь,
# где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
#
# какие вещи взяли все три друга
# какие вещи уникальны, есть только у одного друга
# какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

baggage = {
    'Mark': ('fishing rod', 'lighter', 'tent'),
    'Steeve': ('tent', 'brazier', 'gun'),
    'Axel': ('tent', 'gun', 'sun cream')
}
all_items = list(baggage.values())
must_have_item = set(all_items[0])
for items in all_items:
    must_have_item = must_have_item.intersection(set(items))
print(must_have_item)

uniq_items = {}
for name, items in baggage.items():
    uniq_items[name] = set(items).difference(must_have_item)
print(uniq_items)