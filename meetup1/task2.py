
# Автор Тютин Руслан
# Бот-калькулятор
#
# Научите бота выполнять основные арифметические действия с числами:
# сложение, вычитание, умножение и деление.
# Если боту сказать “2-3=”, он должен ответить “-1”.
# Все выражения для калькулятора должны заканчиваться знаком равно.
# Дополнительно: не забудьте обработать возможные ошибки во вводе: пробелы, отсутствие чисел, деление на ноль.


from telegram.ext import Updater, CommandHandler
import logging, re



TOKEN = open('key_telegrambot', 'r').read()

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('calc', calc))
    updater.start_polling()
    updater.idle()


def calc(bot, update):
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
