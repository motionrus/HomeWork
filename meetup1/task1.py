# Автор Тютин Руслан
#
# Подсчёт количества слов
#
# Добавить команду /wordcount котрая считает сова в присланной фразе.
# Например на запрос /wordcount "Привет как дела" бот должен посчитать
# количество слов в кавычках и ответить: 3 слова.
# Не забудьте: добавить проверки на наличие кавычек, пустую строку. Подумайте, какие еще проверки нужны?

from telegram.ext import Updater, CommandHandler
import logging

TOKEN = open('key_telegrambot', 'r').read()

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('wordcount', wordcount, pass_args=True))
    updater.start_polling()
    updater.idle()


def wordcount(bot, update, args):
    """this function count word(s)"""
    replace_symbol = replace_symbol_quotes(args)
    if validate_line(replace_symbol):
        modify_list = remove_empty_list(replace_symbol)
        count_word = len(modify_list)
        message = 'Total {} word(s)'.format(count_word)
        update.message.reply_text(message)
    else:
        update.message.reply_text('please use next template: /wordcount "any word(s)"')

def replace_symbol_quotes(line):
    """must be list, return symbol " on ' . That's all """
    return [x.replace("'", '"') for x in line]


def remove_empty_list(line):
    try:
        while True:
            line.remove('"')
    except ValueError:
        return line


def validate_line(line):
    """check start and end on symbol " and not empty line"""
    if not line[0].startswith('"'):
        return False
    if not line[-1].endswith('"'):
        return False
    if len(line) == 0:
        return False
    return True


if __name__ == '__main__':
    main()
