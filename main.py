import telebot
from telebot import types

bot = telebot.TeleBot("#")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    key_use = types.InlineKeyboardButton(text='Как использовать продукт', callback_data='use')
    keyboard.add(key_use)
    key_channel = types.InlineKeyboardButton(text='Канал в Telegram', callback_data='channel')
    keyboard.add(key_channel)
    key_chat = types.InlineKeyboardButton(text='Чат-болталка', callback_data='chat')
    keyboard.add(key_chat)
    key_group = types.InlineKeyboardButton(text='Группа в VK', callback_data='group')
    keyboard.add(key_group)
    key_inst = types.InlineKeyboardButton(text='Аккаунт в Instagram', callback_data='inst')
    keyboard.add(key_inst)
    key_site = types.InlineKeyboardButton(text='Посетить сайт марки', callback_data='site')
    keyboard.add(key_site)

    bot.send_message(message.from_user.id, "Привет, " + str(message.from_user.first_name) + "! Чем я могу помочь?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "use":
        bot.send_message(call.message.chat.id, "https://www.youtube.com/channel/UChaTBYD3JEMq_Z_hlZ2PRBQ")
    elif call.data == "channel":
        bot.send_message(call.message.chat.id, "https://t.me/slingme")
    elif call.data == "chat":
        bot.send_message(call.message.chat.id, "https://t.me/slingme_chat")
    elif call.data == "group":
        bot.send_message(call.message.chat.id, "https://vk.com/slingme")
    elif call.data == "inst":
        bot.send_message(call.message.chat.id, "https://www.instagram.com/delezheva_ta/")
    elif call.data == "site":
        bot.send_message(call.message.chat.id, "https://slingme.ru/")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)






bot.polling()