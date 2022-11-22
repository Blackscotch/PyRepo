import random
from statistics import mean
import os

# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

# Создадим таблицу с оценками студентов (количество студентов и оценки в группах - рандом)
def CreateGroups(groups_list: list):
    groups = []
    for i in range(len(groups_list)):
        group_count = random.randint(20,30)
        groups.append([groups_list[i]] + list(random.randint(1,5) for _ in range(group_count)))    
        print(groups[i])
    return groups

# Посчитаем средний балл и выведем название группы
def BestResult(scores_table):
    max = 0
    count = 0
    for items in scores_table:
        items = mean(list(filter(lambda x: str(x).isdigit(),items)))
        print(items)
        if items > max:
            max = items
            x = count
        count += 1
    return f'Победила {scores_table[int(x)][0]} группа с {len(scores_table[x]) - 1} студентами и общим баллом: {round(max, 3)}'

# groups = ['Первая', 'Вторая', 'Третья', 'Четвертая']
# groups_table = CreateGroups(groups)
# print(BestResult(groups_table))
# print()

# input("Нажмите что-нибудь для выполнения след. задачи: ")
# os.system("cls")

# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

def CreateMatrix(count_rows: int):
    matrix = []
    for i in range(count_rows):
        matrix.append(list(random.randint(0,10) for _ in range(count_rows)))
        print(matrix[i])
    return matrix


CreateMatrix(int(input("Введите число: ")))
# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

# Задача 4* (Дополнительная). Реализуйте игру «Поле чудес». Вопрос и правильный ответ сохраните в файл.
# Реализуйте алгоритм шифрования правильного ответа.