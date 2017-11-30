
# Автор Тютин Руслан
# Цикл
#
# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

list_lines = [x for x in range(10)]
for list_line in list_lines:
    print(list_line + 1)
