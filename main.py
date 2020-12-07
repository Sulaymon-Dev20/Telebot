import telebot

from telebot import types

bot = telebot.TeleBot('1496316863:AAFns4Gh4GxapiDcTiZrYsFoBeHmJFQ1zWc')

complaint = ''


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/Hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("✒ Ro`yhatdan o`tish")

    markup.add(item1)
    reply_markup: JSON.stringify({
        hide_keyboard: true
    })
    bot.send_message(message.chat.id,
                     "Assalamu alaykum, {0.first_name}!\nUshbu - <b>{1.first_name}</b>, botdan foydalanishingiz uchun ro`yratdan o`rishingiz kerak 😊".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def register(message):
    if message.text == '✒ Ro`yhatdan o`tish':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("✒ Ariza yozish")
        markup.add(item1)
        if len(message.from_user.first_name) >= 0:
            sti = open('static/Success.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id,
                             text=message.from_user.first_name + " " + message.from_user.last_name + " Siz mofaqyatli ro`yhatdan o`ttingiz 😊,endilikda siz SSD companyasiga murojat qilishingiz mumkin 🧐")
            bot.register_next_step_handler(message, get_text)
        else:
            bot.send_message(message.chat.id, "Error")
    else:
        sti = open('static/Warning.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, 'Ro`yhatdan o`tmasangiz bot ishlamaydi ⚠️')


def get_text(message):
    if message.text == "Ariza yozish":
        bot.send_message(message.from_user.id, "📝")
        bot.send_message(message.from_user.id, "Iltimos Arizangizni batafil ravishda yozing !")
        bot.register_next_step_handler(message, check_text)
    # else:
    #     sti = open('static/Rule.tgs', 'rb')
    #     bot.send_sticker(message.chat.id, sti)
    #     bot.send_message(message.chat.id, 'Iltimos qoyidalarga amal qiling !')
    #     bot.register_next_step_handler(message, get_text)


def check_text(message):
    if len(message.text) > 20:
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Ha ✔", callback_data="Yes")
        key_ok = types.InlineKeyboardButton(text="Yo`q ❌", callback_data="No")
        key_no = types.InlineKeyboardButton(text="Ortga ♻", callback_data="Back")
        keyboard.add(key_yes, key_no, key_ok)
        bot.send_message(message.from_user.id,
                         message.text + "\n⚠️⚠️Arizangizni to`g`ri bo`lsa uni tasdiqlang aks xolda ortga qaytish tugmasini bosing !⚠️⚠️",
                         reply_markup=keyboard)
    else:
        sti = open('static/Warning.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id,
                         "Matn hajmi 20 harfdan ko`proq bo`lishi kerak")
        bot.register_next_step_handler(message, get_text)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Yes":
        bot.send_message(call.message.chat.id, "Yaxshi aka !")
    elif call.data == "No":
        bot.send_message(call.message.chat.id, "try alan")
        bot.send_message(call.message.chat.id, "Qalesan jgar ismin nima ?")
        # bot.send_message(call.message.from_user.id, "what is your name ?")
        bot.register_next_step_handler(call.message, get_text)


bot.polling(none_stop=True)
