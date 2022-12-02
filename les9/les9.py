import telebot
from telebot import types
from metods import *
from random import randint
# Задача 1. Добавьте telegram-боту возможность вычислять выражения:1 + 4 * 2 -> 9

# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

bot = telebot.TeleBot("", parse_mode=None)

markup = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('Помощь')
itembtn2 = types.KeyboardButton('Посчитать')
itembtn3 = types.KeyboardButton('Играть')
markup.add(itembtn1, itembtn2, itembtn3)
digit = 0
count = 0
hint = 0

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, "+ message.from_user.first_name +" "+message.from_user.last_name + ". Тебя приветсвует новый бот. Команды, которые ты можешь ввести, указаны ниже на клавиатуре.", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def check_text(message):
    if 'помощь' in message.text.lower():
        bot.reply_to(message, "/start или /help - вызвать приветсвенное сообщение\n 'играть' - я загадаю число, а ты попробуй отгадать\n 'посчитать' - введи выражение, а я попробую его высчитать.\nПока это все, что я могу :)")
    if 'посчитать' in message.text.lower():
        mess = bot.reply_to(message, "Введи выражение, состоящее из чисел и знаков: \n '*' - умножить\n '/' - делить \n '-' - вычесть \n '+' - сложить")
        bot.register_next_step_handler(mess, ValidText)
    if 'играть' in message.text.lower():
        global digit
        digit = randint(1,1000)
        mess = bot.reply_to(message, f"Я загадал число от 1 до 1000. Как думаешь, что это за число?\nУстанешь гадать, напиши - 'устал'.\nЕще у тебя есть подсказки. Напиши - 'подсказать'.\nПоехали! Вводи число :)")
        bot.register_next_step_handler(message, ValidGema)
def ValidGema(message):
    global digit
    global count
    global hint
    if message.text.isdigit():
        if digit == int(message.text):
            count = count + 1
            bot.reply_to(message, f"Верно! Число ({digit}) угадано с {count} попытки.")
        else:
            count = count + 1
            bot.reply_to(message, f"Не верно! Попробуй еще. Прошло {count} попыток.")
            bot.register_next_step_handler(message, ValidGema)
    elif 'подсказать' in message.text.lower():
        help_me = str(digit)
        if hint == 0:
            hint = hint + 1
            bot.reply_to(message, f"Я загадал {len(help_me)}-значное число.")
        elif hint == 1:
            if len(help_me) > 1:
                hint = hint + 1
                bot.reply_to(message, f"Число начинается с цифры {help_me[0]}")
            else: 
                bot.reply_to(message, f"Число {len(help_me)}-значное. Если не хочешь отгадывать, напиши - 'ответ' и я тебе его скажу.")
        elif hint == 2:
            if len(help_me) > 2:
                hint = hint + 1
                bot.reply_to(message, f"Последняя цифра в числе - это {help_me[2]}")
            else: 
                bot.reply_to(message, f"Число {len(help_me)}-значное и первая цифра {help_me[0]}. Если не хочешь отгадывать, напиши - 'ответ' и я тебе его скажу.")
        else:
           bot.reply_to(message, f"Число {len(help_me)}-значное, первая цифра {help_me[0]} и последняя {help_me[2]}. Если не хочешь отгадывать, напиши - 'ответ' и я тебе его скажу.")     
        bot.register_next_step_handler(message, ValidGema)
    elif 'ответ' in message.text.lower():
        bot.reply_to(message, f"Слабак!! Я загадал число: {digit}")
    elif "устал" in message.text.lower():
        bot.reply_to(message, "Прекращаем игру.")
    else:
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBZGOJ4ulZgcYx7v9-ZGVSjS0PCcIgAAJAAgACz7vUDkUDfp1AfB6zKwQ')
        bot.reply_to(message, "Что-то тут не так. Если хочешь закончить, пиши - 'устал'.\nИли мы будем мучить эту игру бесконечно! Хе-хе-хе)")
        bot.register_next_step_handler(message, ValidGema)
def ValidText(message):
    text = GetList(message.text)
    mess = GetResult(text)
    bot.reply_to(message, f"Результат: {mess}")

bot.infinity_polling()