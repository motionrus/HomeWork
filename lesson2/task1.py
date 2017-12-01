
# Автор Тютин Руслан
# Задание
#
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime, timedelta
import locale, calendar

DATEVIEW = '%d %B %y'
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
date_now = datetime.now()
day_delta = timedelta(days=1)
days_in_mouth = mdays[int(date_now.strftime('%m')) - 1]
mouth_delta = timedelta(days=days_in_mouth)
yesterday = date_now - day_delta
mouth = date_now - mouth_delta

print("Дата вчерашнего дня: {}".format(yesterday.strftime(DATEVIEW)))
print("Сегодня: {}".format(date_now.strftime(DATEVIEW)))
print("Месяц назад: {}".format(mouth.strftime(DATEVIEW)))

str_to_obj = datetime.strptime('01/01/17 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f')

