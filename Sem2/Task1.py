# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

a = 5
print(isinstance(a,int))
print(type(a))
a = 'text'
print(isinstance(a,str))
print(type(a))
a = 5.9
print(isinstance(a,float))
print(type(a))
a = [1, 2, 3]
print(isinstance(a,list))
print(type(a))
a = (1, 2, 3)
print(isinstance(a,tuple))
print(type(a))