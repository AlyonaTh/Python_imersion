# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

dict_counts = {}
new_sorted_dictionary = {}
SHOW_LIMIT = 10

data = input("Input text: ")
marks = ['.', ',', '!', '?', '>', '<', '=', '(', ')']
for i in marks:
    data.replace(i,'')
data = data.upper()
words_list = data.split()
for word in words_list:
    counter = words_list.count(word)
    dict_counts[word] = counter
sorted_values = sorted(dict_counts.values())[::-1]
for i in sorted_values:
    for k in dict_counts.keys():
        if dict_counts[k] == i:
            new_sorted_dictionary[k] = dict_counts[k]
print()
print(list(new_sorted_dictionary.items())[0: SHOW_LIMIT])

