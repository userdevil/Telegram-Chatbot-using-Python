import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import pytube
import re
import shutil

TELEGRAM_TOKEN = '5159256749:AAGXCe1j3yxC-x-i3yBKwznj_-bOIk7JyMw'
stream = ""
url = str("")
bot = telebot.TeleBot(TELEGRAM_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to help to download the youtube just send me the youtube video link\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global stream
    try:
        msg = message.text
        youtub = pytube.YouTube(msg)
        stream = youtub.streams.filter(file_extension='mp4').first().url
        print(youtub.title)
        bot.reply_to(message,youtub.title)
        print(stream)
        bot.reply_to(message,stream)
    except:
        print("An exception occurred")
        bot.reply_to(message,"An exception occurred or send me a correct url if you continueslly getting this error try this app https://codingwithms-60edd.web.app/app.apk")

bot.infinity_polling()
