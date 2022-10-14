# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def TruthTable():
    print("Таблица истинности для ¬(X ∧ Y) ∨ Z")
    print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                tab = not(x and y) or z
                print(f"{x} | {y} | {z} | {int(tab)}")
TruthTable()
input("Нажмите что-нибудь для выполнения следующей задачи:")
print()
# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def IsDigit(data):
    while data.isdigit() == False:
        print("Ошибка ввода. Введите целое число: ")
        data = input()
    return int(data)

def Factorial(digit):
    list = []
    if digit == 0:
        list.extend(1)
    else:
        count = 1
        sum = 1
        for count in range(1, digit+1):
            sum = sum*count
            list.extend([sum])
    return list

def Tusk2():
    start = None
    end = 'конец'
    while end != start:
        number = IsDigit(input("Введите число: "))
        result = Factorial(number)
        print(f"{number} -> {result}")
        start = input("Для продолжения - Enter, для завершения - 'конец': ")

print("Показываем список факториалов числа.")
Tusk2()
print()
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def LikeSymbols(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    list = []
    if len1 < len2:
        for i in range(len1):
            count = 0
            for j in range(len2):
                if str1[i] == str2[j]:
                    count += 1
            list.append(f"{str1[i]} - {count}")
    else:
        for i in range(len2):
            list.append(f"{str2[i]} -> {str1.count(str2[i])}")
    return list

str1 = 'one'
str2 = 'onetwonine'
print(f"Считаем совпадения символов строки '{str1}' в строке '{str2}'")
print(LikeSymbols(str1, str2))
input("Нажмите что-нибудь для выполнения следующей задачи:")
print()

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def ShiftList(array, count):
    len1 = len(array)
    for i in range(len1 - count):
        array = array[1:]+array[:1]
    return array

list = [-3, -2, -1, 0, 1, 2, 3]
print(f"Сдвигаем элементы в списке {list} на 2 позиции вправо")
print(ShiftList(list, 2))
print("На сегнодня это все")


