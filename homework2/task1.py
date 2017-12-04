
# Автор Тютин Руслан
# Задание
#
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime, timedelta
import locale

DATEVIEW = '%d %B %y'

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
day_delta = timedelta(days=1)

yesterday = date_now - day_delta
date_now = datetime.now()
mouth = date_now.replace(month=date_now.month-1)


print("Дата вчерашнего дня: {}".format(yesterday.strftime(DATEVIEW)))
print("Сегодня: {}".format(date_now.strftime(DATEVIEW)))
print("Месяц назад: {}".format(mouth.strftime(DATEVIEW)))

str_to_obj = datetime.strptime('01/01/17 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f')

