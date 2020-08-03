import telebot
import config
from pathlib import Path

bot = telebot.TeleBot(config.TOKEN)
path = Path("C:/Users/v4h4/Desktop/CODIN HOBBY STUFF/small projects/image_comparision_bot")

a = [0,1,2,3]
r = len(a)
middle = len(a)//2

@bot.message_handler(commands=["start"])
def send1(message):
	new_path = "images/"+str(a[0])+".png"
	photo = open(path/new_path, 'rb')
	bot.send_photo(message.chat.id, photo)
	new_path2 = "images/"+str(a[1])+".png"
	photo2 = open(path/new_path2, 'rb')
	bot.send_photo(message.chat.id, photo2)
	bot.send_message(message.chat.id, "Choose "+str(a[0])+" or "+str(a[1]))
	print(a)

@bot.message_handler(commands=["start2"])
def send2(message):
	new_path = "images/"+str(a[len(a)-2])+".png"
	photo = open(path/new_path, 'rb')
	bot.send_photo(message.chat.id, photo)
	new_path2 = "images/"+str(a[len(a)-1])+".png"
	photo2 = open(path/new_path2, 'rb')
	bot.send_photo(message.chat.id, photo2)
	bot.send_message(message.chat.id, "Choose "+str(a[len(a)-2])+" or "+str(a[len(a)-1]))	
	print(a)

@bot.message_handler(content_types=["text"])
def processor(message):
	if len(a)==2:
		del a[0:1]
		a[0]=int(message.text)
		new_path = "images/"+str(a[0])+".png"
		photo = open(path/new_path, 'rb')
		bot.send_photo(message.chat.id, photo)
	elif int(message.text)<middle:
		del a[0:1]
		a[0]=int(message.text)
		send2(message)
	elif int(message.text)>=middle:
		del a[len(a)-2:a[len(a)-1]]
		a.append(int(message.text))
		send1(message)
	
bot.polling()