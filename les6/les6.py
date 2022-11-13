import random
# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

def IsNumber(data):
    while not data.isdigit():
        data = input("Ошибка. Введите натуральное число: ")
    return data

number = IsNumber(input("Введите натуральное число: "))
numbers = int(number) + int(number*2) + int(number*3)
print(numbers)

# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def IsNumberOfHundred(data):
    while True:
        if not data.isdigit():
            data = input("Ошибка. Введите число: ")
        else:
            if len(data) > 3:
               data = input("Ошибка. Введите трехзначное натуральное число: ")
            elif data[0] == "0":
                data = input("Сотни не начинаются с '0'. Введите число: ")
            else: break
    return data

def FindSequenceOfThree(digit: str, list: list):
    list = str(list).replace(", ", "")
    if str(list).find(digit) != -1:
        index = str(list).find(digit)
        return f"В списке есть число {digit}, начинается с {index} элемента в списке."
    else: return f"В списке нет числа {digit}"

list = [random.randint(0, 9) for _ in range(15)]
print(list)    
number = IsNumberOfHundred(input("Введите натуральное число: "))
print(FindSequenceOfThree(number, list))


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
def NodFunc(a, b): 
    if(b == 0):
        return a 
    else: 
        return NodFunc(b, a % b)

list = []
for i in range(2, 12):
    for j in range(1, i):
        if NodFunc(j, i) == 1:
            list.append(f"{j}/{i}")
print("Список простых дробей со знаменателем меньше 11: ")
print(list)