import telebot
from telebot import types
import datetime
from bot_method import *
# from pathlib import Path
# import xml.etree.ElementTree as xml

# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

# 5951329094:AAG8xLgaX_6Zc6QyJGQh3lKuVeNLZsvN3mM


bot = telebot.TeleBot("5951329094:AAG8xLgaX_6Zc6QyJGQh3lKuVeNLZsvN3mM", parse_mode=None)

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.KeyboardButton('Вопрос')
markup.add(itembtn1)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, "+ message.from_user.first_name +" "+message.from_user.last_name + 
        ". Это бот тех. поддержки. Здесь ты можешь задать свой вопрос, на который мы обязательно ответим.\n"
        "Задать вопрос можно, нажав на клавиатуре кнопку 'вопрос' или введя ключевое слово 'вопрос'.", 
        reply_markup=markup
    )
@bot.message_handler(content_types=["text"])
def qust_text(message):
    if 'вопрос' in message.text.lower():
        bot.reply_to(message, "Внимание! Следующее сообщение будет записано и передано в службу поддержки.")
        bot.register_next_step_handler(message, write_text)
def write_text(message):
    if message.text != "":
        mess = message.text
        mess_id = message.message_id
        id = message.from_user.id
        name = message.from_user.first_name
        l_name = message.from_user.last_name
        date = datetime.datetime.now()
        bot.reply_to(message, f"Ваше сообщение было записано и отправлено в тех. поддержку.\n"
            f"Дата обращения: {date.hour}:{date.minute} {date.day}-{date.month}-{date.year}"
        )
        WriteFile(mess_id, mess, id, name, l_name, date)


bot.infinity_polling()