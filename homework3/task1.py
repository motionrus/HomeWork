
# Автор Тютин Руслан
#
# Получение данных
#
# На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных.
# Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json.
# Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows
# https://apidata.mos.ru/v1/datasets/2009/rows?$filter=Cells/Year eq 2015&api_key=d33bff78b7d66eeeadb5b0efca49d5a9

import requests, json
URL = 'https://apidata.mos.ru/v1/datasets/2009/rows'
TOKEN = 'd33bff78b7d66eeeadb5b0efca49d5a9'
SEND_URL = '{}?api_key={}'.format(URL, TOKEN)


def kinder_api(year=None):
    if year:
        global SEND_URL
        SEND_URL += '&$filter=Cells/Year eq ' + str(year)
    print(SEND_URL)
    r = requests.get(SEND_URL)
    if r.status_code == 200:
        return r.json()


# Возвращает файл rows.json в виде объекта
def json_api():
    with open('rows.json', 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    print(kinder_api(year=2017))

