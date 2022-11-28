import telebot

bot = telebot.TeleBot("5951329094:AAG8xLgaX_6Zc6QyJGQh3lKuVeNLZsvN3mM", parse_mode=None)

# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, "Привет. Я только что стартанул. Как дела?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()