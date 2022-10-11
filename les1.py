import code
import math

# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

def WeekNumber():
    start = None
    end = 'конец'
    while end != start:
        digit = input("Введите цифру дня недели: ")
        while digit.isdigit() == False:
            print("Ошибка ввода. Введите цифру от 1 до 7: ")
            digit = input()
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        digit = int(digit)
        match digit:
            case 1:
                print(days[digit-1])
            case 2:
                print(days[digit-1])
            case 3:
                print(days[digit-1])
            case 4:
                print(days[digit-1])
            case 5:
                print(days[digit-1])
            case 6:
                print(days[digit-1])
            case 7:
                print(days[digit-1])
            case _:
                print("Такого дня недели нет.")
        start = input("Напишите 'конец' для выхода или Enter для продолжения: ")

WeekNumber()

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
def input_digit():
    while True:
        myInput = input("Введите число: ")
        try:
            myInput = float(myInput)
        except ValueError:
            print("Ошибка. Число указано неверно, попробуйте еще раз.")
        else:
            break
    return myInput

def Distansce():
    print("Найдем расстояние между двумя точками.")

    print("Введите координаты точки A(x): ")
    ax = input_digit()

    print("Введите координаты точки A(y): ")
    ay = input_digit()

    print("Введите координаты точки B(x): ")
    bx = input_digit()

    print("Введите координаты точки B(y): ")
    by = input_digit()

    if (ax == 0 and ay == 0 and bx == 0 and by == 0) or (ax == bx and ay == by):
        print("Координаты точек A и B совпадают.")
    else:
        distance = math.sqrt(((ax - bx)**2) + ((ay - by)**2))
        distance = round(distance, 2)
        print(f"Расстоянием между А ({ax}, {ay}) и B ({bx}, {by}) равно {distance}")

Distansce()

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0
def QurtOfCoordinate():
    print("Покажем возможное координаты х и у в зависимости от введенной четверти")
    enter = None
    end = 'конец'
    while end != enter:
        while True:
            newInput = input("Введите число от 1 до 4: ")
            try:
                newInput = int(newInput)
                if newInput > 0 and newInput < 5:
                    break
                else:
                    print("Число  не входит в требуемый диапазон.")
            except ValueError:
                print("Ошибка. Число указано неверно, попробуйте еще раз.")
        match newInput:
            case 1:
                print(f"В четверти {newInput} координыты х > 0, y > 0")
            case 2:
                print(f"В четверти {newInput} координыты х > 0, y < 0")
            case 3:
                print(f"В четверти {newInput} координыты х < 0, y < 0")
            case 4:
                print(f"В четверти {newInput} координыты х > 0, y > 0")
        enter = input("Для выхода из программы напишите 'конец', для продолжения Enter: ")

QurtOfCoordinate()  

# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8
def TrueNumbers():
    print("Считаем все четные числа, которые входят в заданное вами число.")
    enter = None
    end = 'конец'
    while end != enter:
        while True:
            digit = input("Введите число: ")
            try:
                digit = int(digit)
                break
            except ValueError:
                print("Ошибка. Число указано неверно, попробуйте еще раз.")
        list = []
        if digit > 1:
            for i in range(1, digit+1):
                if i % 2 == 0 and i > 1:
                    list.extend([i])
                i+=1
            print(f"Введенное число {digit} содержит такие четные числа, как {list}")
        elif digit < -1:
            for i in range(-1, digit-1, -1):
                if i % 2 == 0 and i < -1:
                    list.extend([i])
                i-=1
            print(f"Введенное число {digit} содержит такие четные числа, как {list}")
        else:
            print(f"Указанное число {digit} не содержит четных чисел.")
        enter = input("Для выхода из программы напишите 'конец', для продолжения Enter: ")


TrueNumbers()