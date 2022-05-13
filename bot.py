import telebot
from telebot import types
token='645097492:AAHDWFwmKBnmAlYrbSHlds8lVgWkR0LRGtM'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
  bot.send_message(message.chat.id,"Это - небольшой бот написанный @nekker37")


@bot.message_handler(content_types=["text"])
def start_message(message):
    print(message.text)

    if (message.text.lower().find("нагаторо") != -1):
        photo = open("nagatoro.jpg","rb")
        bot.send_photo(message.chat.id,photo,caption="Нагаторо detected")

    if (message.text.lower().find("лоли") != -1):
        bot.send_photo(message.chat.id,'https://i1.sndcdn.com/artworks-000588837944-wshxw2-t500x500.jpg',caption="Лоли detected")

    else:bot.send_message(message.chat.id, message.text)




bot.infinity_polling()
