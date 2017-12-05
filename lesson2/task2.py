
# Автор Тютин Руслан
# Метро
# В этом задании требуется определить, на каких станциях московского метро
# сейчас идёт ремонт эскалаторов и вывести на экран их названия.
# Файл с данными можно скачать на странице http://data.mos.ru/opendata/624/row/1773539.

import xlrd
from datetime import datetime

TITLE_ESCALATORS = 'Ремонт эскалаторов'
TITLE_STATION = 'Станция метрополитена'
NAME_FILE = 'data-397-2017-10-31.xlsx'


def number_by_name(sheet, title):
    """return number colomn by name cell"""
    for row in range(len(sheet.row(0))):
        if title == sheet.cell(0, row).value:
            return row


open_workbook = xlrd.open_workbook(NAME_FILE)
workbook = open_workbook.sheet_by_index(0)
escalators = number_by_name(workbook, TITLE_ESCALATORS)
station = number_by_name(workbook, TITLE_STATION)

list_date = list()

for w in range(1, len(workbook.col(escalators))):
    range_date = workbook.cell(w, escalators).value
    if not range_date:
        continue
    name_station = workbook.cell(w, station)
    range_date = range_date.split('-')
    datetime.strptime(range_date[0], '%d.%m.%Y')
    first_date, second_date = datetime.strptime(range_date[0], '%d.%m.%Y'), datetime.strptime(range_date[1], '%d.%m.%Y')
    if first_date <= datetime.now() <= second_date:
        print('Эскалатор на станции "{}" не будет работать в период {}-{}.'.format(name_station.value, *range_date))
