from importlib.resources import path
import os
from pathlib import Path

# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def IsDigit(data):
    while not data.isdigit():
        print("Ошибка ввода. Введите целое число: ")
        data = input()
    return int(data)

def Fib(number):
    num1 = num2 = 1
    data = open("fibtext.txt", "w")

    for _ in range(number):
        data.writelines(str(num1)+ "\n")
        num1, num2 = num2, num1 + num2
    
    data.close()
print("Выполняется задача 1")
num = IsDigit(input("Укажите число: "))
Fib(num)
input("Результат метода можно найти в файле, а для выполнения следующей задачи нажмите Enter")
os.system("cls")

# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def GetFruitFromFile(letter):
    path = Path("les3", "fruit.txt")
    data = open(path, "r", encoding = "utf-8")
    fruitlist = []
    for text in data:
        text = ''.join(filter(str.isalpha, text)).lower()
        if text[0] == letter:
            fruitlist.append(text)
    data.close()
    return fruitlist
print("Выполняется задача 2")
letter = input("Введите любую букву: ").lower()
print(f"Фрукты на букву '{letter}' это: {GetFruitFromFile(letter)}")
input("Для выполнения следующей задачи нажмите Enter")
os.system("cls")

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

dictionary = {
    "Привет": "И тебе привет (^_^)",
    "Как тебя зовут?": "Я обычно сам прихожу, но можешь называть меня - Моб)",
    "Пока": "Удачи :)"
}

exit, say = "Пока", ""
while exit != say:
    say = input("Вы: ")
    if say in dictionary.keys():
        print(f"Моб: {dictionary[say]}")
    else:
        print("Моб: Я не знаю ответ. Подскажешь?")
        yes = "Да"
        answer = input("Да или Нет? ")
        if answer == yes:
            newKey = input(f"На фразу '{say}' нужно ответить: ")
            dictionary[say] = newKey
            print("Моб: Спасибо, что научил чему-то новому :)")
        else:
            print("Моб: Ну и пожалуйста ('_')")