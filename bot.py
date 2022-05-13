import telebot
from telebot import types
import requests
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

@bot.message_handler(content_types=["photo"])
def photo_save(message):
    id = message.photo[-1].file_id
    print("Скачан файл с ID:",id)
    file_info = bot.get_file(id)
    path = "SavedPhoto/" + id +".jpg"
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path,'wb') as new_file:
        new_file.write(downloaded_file)


bot.infinity_polling()
