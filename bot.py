import telebot
from telebot import types
import requests
token='645097492:AAHDWFwmKBnmAlYrbSHlds8lVgWkR0LRGtM'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start_message(message):
  bot.send_message(message.chat.id,
  """
  Это - небольшой бот написанный @nekker37
  Сюда можно отправлять фото, которые потом весьма успешно сохранятся на сервере.
  """)




@bot.message_handler(content_types=["text"])
def start_message(message):
    print(message.text)
    if (message.text.lower().find("нагаторо") != -1):
        photo = open("nagatoro.jpg","rb")
        bot.send_photo(message.chat.id,photo,caption="Нагаторо detected")
    if (message.text.lower().find("лоли") != -1):
        bot.send_photo(message.chat.id,'https://i1.sndcdn.com/artworks-000588837944-wshxw2-t500x500.jpg',caption="Лоли detected")
    if (message.text.lower().find("лабы") != -1):
        bot.send_photo(message.chat.id,open("laby.jpg","rb"),caption="Вот мои ебучие лабы на момент 17/5/22 11:15")
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
    bot.send_message(message.chat.id, 'Фото успешно сохранено.')


@bot.message_handler(content_types=["document"])
def photo_save(message):
    id = message.document.file_id
    print("Скачан файл с ID:",id)
    file_info = bot.get_file(id)
    path = "SavedDocument/" + message.document.file_name
    downloaded_file = bot.download_file(file_info.file_path)
    with open(path,'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, 'Документ успешно сохранён.')




bot.infinity_polling()
