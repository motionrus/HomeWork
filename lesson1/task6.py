
# Автор Тютин Руслан
#
# Цикл while (https://learn.python.ru/lessons/11_while.html?full#8)
# Смотреть task7.py. Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
# пока не встретите имя "Валера". Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()
# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.
# Смотреть task8.py Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя
# “Как дела?”, пока он не ответит “Хорошо”
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

answeres = {
    "привет": "привет",
    "что нового": "ничего",
    "что старого": "спроси еще что нибудь"
}
names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]


def find_person(name):
    while True:
        if names.pop() == name:
            return "{} нашелся".format(name)
        if len(names) == 0:
            return "{} не нашелся".format(name)


print(find_person("Петя"))


def ask_user():
    while True:
        question = input("Спроси что-нибудь: ")
        if question == "Пока!":
            break
        answer = answeres.get(question)
        print(answer)


if __name__ == '__main__':
    ask_user()
