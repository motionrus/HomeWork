
# Автор Тютин Руслан
# Задание
#
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import datetime, timedelta
import locale

DATEVIEW = '%d %B %y'
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
dt_now = datetime.now()
day_delta = timedelta(days=1)
day_in_mounth = mdays[int(dt_now.strftime('%m')) - 1]
mounth_delta = timedelta(days=day_in_mounth)
yestarday = dt_now - day_delta
mounth = dt_now - mounth_delta

print("Дата вчерашнего дня: {}".format(yestarday.strftime(DATEVIEW)))
print("Сегодня: {}".format(dt_now.strftime(DATEVIEW)))
print("Месяц назад: {}".format(mounth.strftime(DATEVIEW)))

str_to_obj = datetime.strptime('01/01/17 12:10:03.234567', '%d/%m/%y %H:%M:%S.%f')