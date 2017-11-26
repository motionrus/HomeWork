
# Автор Тютин Руслан
# Задание
#
# Переписать функцию ask_user (), добавив обработка exception-ов
# Добавить перехват ctrl + C и прощание

def ask_user():
    while True:
        try:
            ask = input("Как дела?: ")
            if ask == 'Хорошо':
                return
        except KeyboardInterrupt:
            print("Вы нажали Ctrl + C программа будет завершена, всего доброго")
            break

ask_user()