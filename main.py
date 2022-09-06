import os
import telebot
import requests

#API_KEY = os.getenv('API_KEY')   // Some problems with this part, probably because its multithreaded or async
#                                 // Exception: Bot token is not defined

bot = telebot.TeleBot("MY_TOKEN")

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey!")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['compliment'])
def compliment(message):
    response = requests.get("https://complimentr.com/api")
    bot.reply_to(message, response.json()['compliment'])



def wassup(message):
    if message.text == "wassup":
        return True
    else:
        return False

@bot.message_handler(func=wassup)
def wazzupp(message):
    bot.send_message(message.chat.id, "Wazzupp!")

bot.infinity_polling()