import telebot
from telebot import types
from metods import *
# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

bot = telebot.TeleBot("", parse_mode=None)

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
        mess = bot.reply_to(message, "Введи выражение, состоящее из чисел и знаков: \n '*' - умножить\n '/' - делить \n '-' - вычесть \n '+' - сложить")
        bot.register_next_step_handler(mess, ValidText)
def ValidText(message):
    text = GetList(message.text)
    mess = GetResult(text)
    bot.reply_to(message, f"Результат: {mess}")
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.infinity_polling()