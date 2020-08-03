import config
import telebot
import os
import random
from telebot import types
import time
import database_connection


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Welcome to guess song game! type: /play")

@bot.message_handler(commands=['play'])
def send_music(message):
    counter = 0
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            c = database_connection.create_connection("db_0.db")
            list_of_music = database_connection.select_all_rows(c)
            bot.reply_to(msg, str(counter)+' '+list_of_music[counter][2]+', '+list_of_music[counter][3])
            counter+=1
    bot.send_message(message.chat.id, r"Answer like this: 0 Imagine Dragons where 0 is number of song and name")    

        
@bot.message_handler(content_types=['text'])
def input_handler(message):
    if message.text=="0 Imagine Dragons":
        bot.reply_to(message, "hurray")    
    elif message.text=="1 AM":
        bot.reply_to(message, "hurray")
    elif message.text=="2 wheres my mind":
        bot.reply_to(message, "hurray")
    elif message.text=="3 i dont know":
        bot.reply_to(message, "hurray")
    elif message.text=="4 i dont know 2":
        bot.reply_to(message, "hurray")
    else:
        bot.reply_to(message, "wrong")
        
if __name__=="__main__":
    bot.infinity_polling()
