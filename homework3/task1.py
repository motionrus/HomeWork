
# Автор Тютин Руслан
#
# Получение данных
#
# На сайте портала открытых данных Москвы есть таблица с популярными именами новорожденных.
# Напишите функцию, которая получает данные при помощи requests и читает содержимое в формате json.
# Для получения данных используйте ссылку http://api.data.mos.ru/v1/datasets/2009/rows
# https://apidata.mos.ru/v1/datasets/2009/rows?$filter=Cells/Year eq 2015&api_key=d33bff78b7d66eeeadb5b0efca49d5a9

import requests, json
from datetime import datetime
URL = 'https://apidata.mos.ru/v1/datasets/2009/rows'
TOKEN = 'd33bff78b7d66eeeadb5b0efca49d5a9'
SEND_URL = '{}?api_key={}'.format(URL, TOKEN)


def kinder_api(year=None):
    send_url = SEND_URL
    if year:
        send_url += '&$filter=Cells/Year eq ' + year
    date_now = datetime.now().strftime('%d/%h/%Y %H:%M:%S')
    print('*[{}] SEND URL "{}"'.format(date_now, send_url))
    r = requests.get(send_url)
    if r.status_code == 200:
        return r.json()


# Возвращает файл rows.json в виде объекта list
def json_api(year=None):
    with open('rows.json', 'r', encoding='utf-8') as f:
        if year:
            json_list = json.load(f)
            return [j for j in json_list if str(j['Cells']['Year']) == year]
        return json.load(f)


if __name__ == "__main__":
    print(kinder_api(year=2017))

