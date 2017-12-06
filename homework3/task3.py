
# Автор Тютин Руслан
#
# Фильтрация данных
# Ограничьте выводимые данные одним годом. Год должен указываться в URL как параметр, например /names?year=2016.


from task1 import kinder_api
from flask import Flask, render_template

YEAR = [2015, 2016, 2017]
app = Flask(__name__)


@app.route("/names/<int:year>")
@app.route("/names")
def names(year=None):
    if year not in YEAR:
        year = None
    list_data = list()
    for j in kinder_api(year):
        json_data = dict()
        json_data['name'] = j['Cells']['Name']
        json_data['year'] = j['Cells']['Year']
        json_data['month'] = j['Cells']['Month']
        json_data['count'] = j['Cells']['NumberOfPersons']
        list_data.append(json_data)
    return render_template('table.html', datas=list_data, len_data=len(list_data))


@app.route("/")
def main():
    return render_template('index.html', years=YEAR)


if __name__ == "__main__":
    app.run()
