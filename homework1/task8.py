
# Автор Тютин Руслан
#
# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”


def ask_user():
    while True:
        answer = input("Как дела?: ")
        if answer == 'Хорошо':
            return


ask_user()
