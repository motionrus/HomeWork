
# Автор Тютин Руслан
# Задание
#
# Скачайте файл по ссылке
# Прочитайте его и подсчитайте количество слов в тексте


count_line = int()
with open('referat.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        count_line += len(line.split())

print('В файле {} слов(а)'.format(count_line))
