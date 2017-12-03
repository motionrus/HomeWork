
# Автор: Тютин Руслан
# Оценки
#
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.


school_lists = [
        {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
        {'school_class': '5a', 'scores': [3, 4, 3, 5, 2]},
        {'school_class': '6a', 'scores': [3, 5, 4, 5, 2]},
        {'school_class': '7a', 'scores': [3, 4, 4, 2, 2]},
        {'school_class': '8a', 'scores': [3, 3, 4, 5, 2]},
        {'school_class': '9a', 'scores': [3, 5, 4, 5, 2]}
]
middle_lists = []


for school_list in school_lists:
    score_list = school_list['scores']
    middle = sum(score_list)/len(score_list)
    print("average in class {}: {}".format(score_list, middle))
    middle_lists.append(middle)
middle_school = sum(middle_lists)/len(middle_lists)
print("middle for school: {}".format(middle_school))
