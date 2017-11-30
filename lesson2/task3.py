
# Автор Тютин Руслан
# Задание
#
# Возьмите словарь с ответами из функции get_answer
# Запишите его содержимое в формате csv в формате: "ключ"; "значение". Каждая пара ключ-значение должна располагаться на отдельной строке

import csv
answeres = {
    "привет": "привет",
    "что нового": "ничего",
    "что старого": "спроси еще что нибудь"
}




with open('export.csv', 'w') as f:
    writer = csv.DictWriter(f, ['key', 'value'], )
    writer.writeheader()
    for key in answeres:
        writer.writerow({'key': key, 'value': answeres[key]})
