import telebot
from telebot import types

bot=telebot.TeleBot('8445056578:AAGtI5bLF_hTJHwC0Xn_fxIz-ehhuTKlRwo')

@bot.message_handler(commands=['start'])
def main(message):
    if message.from_user.last_name != None:
        bot.send_message(message.chat.id, f'{message.from_user.last_name} {message.from_user.first_name} приветствуем в нашей сетки Телеграмм Каналов Пропишите "/help" что-бы узнать все возможности бота.')
    elif message.from_user.last_name == None:
        bot.send_message(message.chat.id, f'{message.from_user.first_name} приветствуем в нашей сетки Телеграмм Каналов  Пропишите "/help" что-бы узнать все возможности бота.')


@bot.message_handler(commands=['help'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Ссылки на каналы сетки', callback_data='Kanals')
    btn2 = types.InlineKeyboardButton('Ссылки на чаты сетки', callback_data='Chats')
    btn3 = types.InlineKeyboardButton('Стать администратором чата сетки', callback_data='ADMKanals')
    btn4 = types.InlineKeyboardButton('Стать администратором канала сетки', callback_data='ADMChats')
    markup.row(btn1, btn2)
    markup.row(btn3)
    markup.row(btn4)
    bot.reply_to(message, 'Большая часть функций вызывается кнопками под этим сообщением.  Жалобы на администраторов вызывается командой /report', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    if callback.data == 'Kanals':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1. 𝐒𝐮𝐧𝐚𝐩𝐬𝐞 𝐇𝐮𝐛', url='https://t.me/Sunapse_Hub')
        markup.row(btn1)
        bot.edit_message_text('Ссылки на каналы сетки:', callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback == 'Chats':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1. 𝐒𝐮𝐧𝐚𝐩𝐬𝐞 𝐇𝐮𝐛', url='https://t.me/Sunapse_Hub')
        markup.row(btn1)
        bot.edit_message_text('Ссылки на чаты сетки:', callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback == 'ADMKanals':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1. 𝐒𝐮𝐧𝐚𝐩𝐬𝐞 𝐇𝐮𝐛', url='https://t.me/Sunapse_Hub')
        markup.row(btn1)
        bot.edit_message_text('Стать администратором чата сетки:', callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback == 'ADMChats':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1. 𝐒𝐮𝐧𝐚𝐩𝐬𝐞 𝐇𝐮𝐛', url='https://t.me/Sunapse_Hub')
        markup.row(btn1)
        bot.edit_message_text('Стать администратором канала сетки:', callback.message.chat.id, callback.message.message_id, reply_markup=markup)


bot.polling(none_stop=True)