
# Автор Тютин Руслан
# Сравнение строк (https://learn.python.ru/lessons/10_if.html?full#11)
#
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.


def compare_line(first, second):
    if validate_line(first) and validate_line(second):
        if first == second:
            return 1
        if second == "learn":
            return 3
        if len(first) > len(second):
            return 2
    else:
        return 'Ошибка валидации строки!'

def validate_line(line):
    '''Эта функция проверяет что line это строка и она не равна None'''
    if type(line) == 'str' and line != '':
        return True

    return False

print(compare_line("example", "learn"))