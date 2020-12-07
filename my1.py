import telebot
from telebot import types

# 1496316863:AAFns4Gh4GxapiDcTiZrYsFoBeHmJFQ1zWc

bot = telebot.TeleBot('1496316863:AAFns4Gh4GxapiDcTiZrYsFoBeHmJFQ1zWc')

name = ''
surName = ''
age = 0


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom bratishka Alloh o`zganishini onson qilsin in shaa Alloh hamma yaxshi bo`ladi!")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "asdf":
        bot.reply_to(message, "ASDFASFASDFSADFDF")
    elif message.text == "Jinni":
        bot.reply_to(message, "Ahmoq 😛")
        bot.reply_to(message, "😛")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "what is your name ?")
        bot.register_next_step_handler(message, get_name)
    # bot.reply_to(message,message.text)


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "what is your surName?")
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surName
    surName = message.text
    bot.send_message(message.from_user.id, "Yoshingizni kiriting!")
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Yoshingizni sonda kiriting !")
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Yes2", callback_data="Yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="No", callback_data="No")
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, "Yur name " + name + " your surname " + surName + " your age " + str(age),                     reply_markup=keyboard)
    # bot.register_next_step_handler(message, req_ok)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Yes":
        bot.send_message(call.message.chat.id, "Yaxshi aka !")
    elif call.data == "No":
        bot.send_message(call.message.chat.id, "try alan")
        bot.send_message(call.message.chat.id, "Qalesan jgar ismin nima ?")
        # bot.send_message(call.message.from_user.id, "what is your name ?")
        bot.register_next_step_handler(call.message, get_name)

bot.polling()
