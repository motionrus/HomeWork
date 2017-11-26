
# Автор Тютин Руслан

# Цикл while (https://learn.python.ru/lessons/11_while.html?full#8)
# Смотреть task7.py. Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
# Смотреть task8.py Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

answeres = {
    "привет": "привет",
    "что нового": "ничего",
    "что старого": "спроси еще что нибудь"
}

names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
    while True:
        if names[-1] == name:
            break
        if len(names) == 1:
            return "{} не нашелся".format(name)
        names.pop()
    return "{} нашелся".format(name)

print (find_person("Петя"))

def get_answer(key, answeres):
    return answeres.get(key)

def ask_user(name = ""):
    while True:
        key = input("Спроси что-нибудь: ")
        if key == "Пока!":
            break
        answer = get_answer(key, answeres)
        print(answer)
ask_user()