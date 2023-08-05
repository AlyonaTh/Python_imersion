'''
Задание №1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
Добавьте  строки документации для классов.
'''
import datetime


class MyStr(str):
    """
    My class  comment
    """
    d = 5

    def __new__(cls, value, author_name):
        """
        Create example
        :param value:
        :param author_name:
        creation_time = datetime.datetime.now()
        """
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.creation_time = datetime.datetime.now()
        return instance


if __name__ == '__main__':

    s = MyStr("Text", 'Alyona')
    print(s, s.author_name, s.creation_time)
    print(s.upper())

    print(MyStr.__doc__)
    print(MyStr.__new__.__doc__)
    print(help(MyStr))