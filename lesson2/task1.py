
# Автор Тютин Руслан
# Остановки
#
# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок,
# вывести улицу, на которой больше всего остановок.
from collections import Counter
import csv


list_stop_bus = list()
list_street = list()
with open('data-398-2017-12-01.csv', 'r', encoding='cp1251') as f:
    reader = csv.DictReader(f, delimiter=";")
    for r in reader:
        list_stop_bus.append(r['StationName'])
        list_street.append(r['Street'])


count_bus_stop = len(set(list_stop_bus))
max_bus_stop = Counter(list_stop_bus).most_common()[0]
max_count_street = Counter(list_street).most_common()[1]


print('Количество остановок в г.Москва: {}'.format(count_bus_stop))
print('На улице: "{}", больше всего остановок: "{}"'.format(max_count_street[0], max_count_street[1]))
print('')
print('Не по заданию, на в качестве бонуса.')
print('Больше всех остановок с названием: "{}". Их количество: "{}"'.format(max_bus_stop[0], max_bus_stop[1]))
