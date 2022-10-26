from math import sqrt
from math import pi
import os
from importlib.resources import path
from pathlib import Path


# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

def IsDigit(data):
    while not data.isdigit():
        print("Ошибка ввода. Введите целое число: ")
        data = input()
    return int(data)

def SimplMultipliers(digit):
    multipliers = []
    while (digit % 2 == 0):
        multipliers.append(2)
        digit = digit / 2
    for i in range(3, int(sqrt(digit)) + 1, 2):
        while digit % i == 0:
            multipliers.append(i)
            digit = digit / i
    if digit > 2:
        multipliers.append(int(digit))
    return multipliers
# print("Выполняется задача 1")
# digit = IsDigit(input("Задайте натуральное число: "))
# print(f"Список делителей {digit}: {SimplMultipliers(digit)}")
# input("Для выполнения следующей задачи нажмите Enter")
# os.system("cls")

# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

# print("Выполняется задача 2")
# path = Path("les4", "file.txt")
# data = open(path, "r", encoding = "utf-8")
# info = data.readlines()
# data.close()

# assortment = set(info[0].replace("\n", "").split(", "))
# instock = set(info[1].replace("\n", "").split(", "))
# need = assortment.difference(instock)
# print(f"На складе осутствует {need}")
# input("Для выполнения следующей задачи нажмите Enter")
# os.system("cls")

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа. 3 -> 3.142
# 5 -> 3.14159

# print("Выполняется задача 3")
# point = IsDigit(input("Задайте точность числа π: "))
# print(f"Число π с точностью {point} это: {round(pi, point)}")
# input("Для выполнения следующей задачи нажмите Enter")
# os.system("cls")

# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# Результат: 8x^2 + 4x + 8

def OpenFile(path):  
    data = open(path, "r", encoding = "utf-8")
    info = data.readlines()
    data.close()
    return info

print("Выполняется задача 4")
path1 = Path("les4", "mn1.txt")
path2 = Path("les4", "mn2.txt")



mn1 = str(OpenFile(path1)).strip("'[] ")
mn2 = str(OpenFile(path2)).strip("'[] ")

for i in mn1:
    print(i)




