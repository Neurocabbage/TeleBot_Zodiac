import telebot
from config import TOKEN
import random
bot = telebot.TeleBot(TOKEN)


"""Команда СТАРТ"""


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Знак Зодиака')
    item2 = telebot.types.KeyboardButton('Угадайка')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Добро пожаловать! Выберите нужный вам пункт меню: ', reply_markup=markup)


def random_number(message):
    x = str(random.randint(1, 3))
    if message.text == x:
        bot.send_message(message.chat.id, f'ты угадал мое число {x}')
    else:
        bot.send_message(message.chat.id, 'не угадал')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'Привет, как дела?')
    elif message.text == 'Знак Зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item_1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item_2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item_3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        item_4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item_5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item_6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item_7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item_8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item_9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item_10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item_11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item_12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(item_1, item_2, item_3,item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11, item_12)
        bot.send_message(message.chat.id, 'Выбирай', reply_markup=markup)
    elif message.text == 'Угадайка':
        msg = bot.send_message(message.chat.id, 'Я загадал число от 1 до 3, попробуй угадай')
        bot.register_next_step_handler(msg, random_number)
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHLTdjuu3rY_j1bKp4I6ovh0-fJ_0Q7QACGAADeXHeFlkmTdPzTa_tLQQ')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dict_znak = znak_char()
    if call.data == 'Овен':
        bot.send_message(call.message.chat.id, dict_znak['Овен'])
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, dict_znak['Телец'])
    elif call.data == 'Близнецы':
        bot.send_message(call.message.chat.id, dict_znak['Близнецы'])
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, dict_znak['Рак'])
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, dict_znak['Лев'])
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, dict_znak['Дева'])
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, dict_znak['Весы'])
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, dict_znak['Скорпион'])
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, dict_znak['Стрелец'])
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, dict_znak['Козерог'])
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, dict_znak['Водолей'])
    elif call.data == 'Рыбы':
        bot.send_message(call.message.chat.id, dict_znak['Рыбы'])

def znak_char():
    dict = {}
    with open('text.txt', 'r', encoding='utf-8') as file:
        for i in range(12):
            str1= file.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
    return dict



bot.polling(none_stop=True)