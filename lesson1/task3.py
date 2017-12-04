
# Автор Тютин Руслан
# Бот-калькулятор(бонусное задание)
#
# Смотреть task2.py
# Научите бота выполнять основные арифметические действия с числами:
# сложение, вычитание, умножение и деление.
# Если боту сказать “2-3=”, он должен ответить “-1”.
# Все выражения для калькулятора должны заканчиваться знаком равно.
# Дополнительно: не забудьте обработать возможные ошибки во вводе: пробелы, отсутствие чисел, деление на ноль.
#
# Бонусное задание: клавиатура
# Добавьте к предыдущей задаче клавиатуру калькулятора с цифрами и основными математическими действиями.



from telegram.ext import Updater, CommandHandler
import telegram
import logging, re, pickle

with open('telegrambot_token', 'rb') as f:
    TOKEN = pickle.load(f)
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('calc', calc))
    updater.start_polling()
    updater.idle()


def start(bot, update):
    custom_keyboard = [
        ['7', '8', '9', '*', ],
        ['4', '5', '6', '/', ],
        ['1', '2', '3', '-', ],
        ['0', '.', '=', '+', ],
    ]
    #custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    print(bot.get_updates())
    chat_id = bot.get_updates()[-1].message.chat_id
    bot.send_message(chat_id=chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup
                     )


def calc(bot, update):
    custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    chat_id = bot.get_updates()[-1].message.chat_id
    bot.send_message(chat_id=chat_id,
                     text="Custom Keyboard Test",
                     reply_markup=reply_markup)
    try:
        expr = list(re.findall(r'(\d+)([+-/*])(\d+)(=)$', update.message.text)[0])
    except:
        return update.message.reply_text('выражение не совпадает с шаблоном "2-3="')
    expr[0],expr[2] = int(expr[0]), int(expr[2])
    # for example ["43242", "+", "4224", "="]
    if validate_expr_zero(expr):
        return update.message.reply_text('Деление на ноль')
    if expr[1] == '+':
        return update.message.reply_text(expr[0] + expr[2])
    if expr[1] == '-':
        return update.message.reply_text(expr[0] - expr[2])
    if expr[1] == '*':
        return update.message.reply_text(expr[0] * expr[2])
    if expr[1] == '/':
        return update.message.reply_text(expr[0] / expr[2])


def validate_expr_zero(expr):
    if expr[1] == '/' and expr[2] == '0':
        return True

main()
