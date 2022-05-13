import telebot
from telebot import types
token='645097492:AAHDWFwmKBnmAlYrbSHlds8lVgWkR0LRGtM'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
  bot.send_message(message.chat.id,"Это - небольшой бот написанный @nekker37")


@bot.message_handler(content_types=["text"])
def start_message(message):
  bot.send_message(message.chat.id, message.text)




bot.infinity_polling()
