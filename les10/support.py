import telebot
from telebot import types
import datetime
from bot_method import *

bot = telebot.TeleBot("5951329094:AAG8xLgaX_6Zc6QyJGQh3lKuVeNLZsvN3mM", parse_mode=None)

new_list = ReadFile()
if len(new_list) > 0:
    for items in new_list:
        new_answer = "" 
        print()
        print(f"Сообщение №{items[0]} от пользователя {items[3]} {items[4]} (id = {items[2]})")
        print(f"текст сообщения: '{items[1]}'")
        print()
        new_answer = input("Ваш ответ: ")
        if new_answer != "":
            bot.send_message(items[2], f"Здравствуйте, {items[3]} {items[4]}.\n"
                f"Вы задавали вопрос: {items[1]}\n"
                f"Ответ: {new_answer}"
            )
    RewriteFile()
else:
    print("Пока нет ни одного вопроса от пользователей.")
    