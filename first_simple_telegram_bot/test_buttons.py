from telebot import types
import telebot
import config

bot = telebot.TeleBot(config.token)

def buttons():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    btn0 = types.KeyboardButton("BUTTON")
    btn1 = types.KeyboardButton("BUTTON1")
    btn2 = types.KeyboardButton("BUTTON2")
    btn3 = types.KeyboardButton("BUTTON3")
    btn4 = types.KeyboardButton("BUTTON4")
    btn5 = types.KeyboardButton("BUTTON5")
    markup.add(btn0, btn1, btn2, btn3, btn4, btn5)
    return markup

@bot.message_handler(commands=['start'])
def button(message):
    bot.send_message(message.chat.id, "Choose one button", reply_markup=buttons())

@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text=="BUTTON":
        bot.send_message(message.chat.id, "YAY ! ! !")    
    else:
        bot.send_message(message.chat.id, "((((((")

bot.polling()


