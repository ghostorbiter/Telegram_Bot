import os
import telebot

#API_KEY = os.getenv('API_KEY')   // Some problems with this part, probably because its multithreaded or async
#                                 // Exception: Bot token is not defined

bot = telebot.TeleBot("MY_TOKEN")

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey!")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")



def wassup(message):
    if message.text == "wassup":
        return True
    else:
        return False

@bot.message_handler(func=wassup)
def wazzupp(message):
    bot.send_message(message.chat.id, "Wazzupp!")

bot.infinity_polling()