

# Задание
#
# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
# При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import datetime
import ephem

KEY = open('key_telegrambot', 'r').read()

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    updater = Updater(KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", planet))
    updater.start_polling()
    updater.idle()


def greet_user(bot, update):
    print(update)
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet(bot, update):
    name_planet = update.message.text.split()[1]
    d = datetime.datetime.now()
    date_now = d.strftime("%Y/%m/%d")
    if name_planet == 'Venus':
        module_planet = ephem.Venus(date_now)
        result = ephem.constellation(module_planet)[1]
        format_result = 'на {} число {} находится в созведии {}'.format(date_now, name_planet, result)
        update.message.reply_text(format_result)
    if name_planet == 'Mars':
        module_planet = ephem.Mars(date_now)
        result = ephem.constellation(module_planet)[1]
        format_result = 'на {} число {} находится в созведии {}'.format(date_now, name_planet, result)
        update.message.reply_text(format_result)

    update.message.reply_text('Ты можешь набрать "/planet Venus" или "/planet Mars"')

main()