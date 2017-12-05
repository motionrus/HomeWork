
# Автор Тютин Руслан
#
# Вывод данных на сайте
#
# Добавьте на сайт страницу /names, на которой в табличном виде выведите данные о именах новорожденных,
# получаемые при помощи функции из предыдущей задачи.
# Пример простейшего оформления таблицы - на следущейм слайде.


import requests
from task1 import kinder_api, json_api
from flask import Flask, jsonify, render_template

#my_json = kinder_api()

app = Flask(__name__)

@app.route("/names")
def names():
    list_data = list()
    for j in json_api():
        print(j)
        json_data = dict()
        json_data['name'] = j['Cells']['Name']
        json_data['year'] = j['Cells']['Year']
        json_data['month'] = j['Cells']['Month']
        list_data.append(json_data)
    print(list_data)
    return render_template('template.html', datas=list_data)

if __name__ == "__main__":
    app.run()