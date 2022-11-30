import telebot
from telebot import types
# 5951329094:AAG8xLgaX_6Zc6QyJGQh3lKuVeNLZsvN3mM
# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

bot = telebot.TeleBot("5951329094:AAG8xLgaX_6Zc6QyJGQh3lKuVeNLZsvN3mM", parse_mode=None)

markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('Помощь')
itembtn2 = types.KeyboardButton('Посчитать')
itembtn3 = types.KeyboardButton('Играть')
markup.add(itembtn1, itembtn2, itembtn3)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, "+ message.from_user.first_name +" "+message.from_user.last_name + ". Тебя приветсвует новый бот. Команды, которые ты можешь ввести, указаны ниже на клавиатуре.", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def check_text(message):
    if 'посчитать' in message.text.lower():
        mess = bot.reply_to(message, "Введи выражение: ")
        bot.register_next_step_handler(mess, test)
def test(message):
    if '1+1' in message.text:
        bot.reply_to(message, "Верно")
    else: bot.reply_to(message, "Не верно")
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.infinity_polling()