# Задача 1
# В модуль с проверкой даты  добавьте возможность запуска в терминале с передачей даты на проверку. .


from m_module import calendar, calendar_tetminal


if __name__ == '__main__':
    print(calendar(input("Enter date dd.mm.yyyyy: ")))
    calend_tetminal()