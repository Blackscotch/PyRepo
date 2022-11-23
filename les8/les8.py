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

def SumMatrix(matrix):
    rows = len(matrix)
    diag_sum = 0
    sum_rows = []
    for i in range(rows):
        suma = 0
        for x in range(rows):
            suma += matrix[i][x]
            if i == x:
                diag_sum += matrix[i][x]
        sum_rows.append(suma)

    itog = []
    for i in range(rows):
        if sum_rows[i] > diag_sum:
            itog.append(i+1)
    
    if len(itog) < 1:
        return f"В матрице нет строк, превышающих сумму диагонали, равную {diag_sum}"
    elif len(itog) == 4:
        return f"Все строки в матрице превышают сумму диагонали, равную {diag_sum}"
    else:
        return f"{itog} строки превышают сумму диагонали, равную {diag_sum}"

# matrix = CreateMatrix(int(input("Введите размер матрицы: ")))
# print(SumMatrix(matrix))

# print()

# input("Нажмите что-нибудь для выполнения след. задачи: ")
# os.system("cls")

# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

# Метод рассчитает и заполнит количество дней для каждого месяца и температуру, темп. - рандом.
def CreateWether(month):
    wether = []
    month_count = 0
    for i in range(len(month)):
        if month[i] == "Февраль":
            month_count = random.randint(28,29)
        elif month[i] == "Апрель" or month[i] == "Июнь" or month[i] == "Сентябрь" or month[i] == "Ноябрь":
            month_count = 30
        else: month_count = 31
        wether.append(list(random.randint(-10,32) for _ in range(month_count)))
        print(wether[i])
    return wether

# Транформируем все в один список и возвращаем
def TransforWether(month):
    days = []
    for items in month:
        days.append(items)
    return days

def FindMothLen():
    count_days = []
    summa = 0
    for month in wether:
        summa += len(month)
        print(len(month))
        count_days.append(summa - 1)
    return count_days

# Находим индекс максимально высокой температуры в заданном диапазане и возвращаем
def FindMaxIndex(days, interval):
    max = 0
    max_index = 0
    for i in range(len(days) - interval):
        if max < sum(days[i:i+interval]):
            max = sum(days[i:i+interval])
            max_index = i
    print(max_index)
    return max_index

month = ['Май', 'Июнь', 'Июль', 'Август', 'Сентябрь']
wether = CreateWether(month)
interval = 7

count_days = {}
    


# count = []
# long_wet = []
# summa = 0
# for mons in wether:
#     print(len(mons))
#     summa += len(mons)
#     count.append(summa - 1)
#     # for x in mons:
#     #     long_wet.append(x)
# # print(count, len(long_wet)) 

# 
# max = 0
# max_index = 0
# for i in range(len(long_wet) - interval):
#     if max < sum(long_wet[i:i+interval]):
#         max = sum(long_wet[i:i+interval])
#         max_index = i
# print(max_index)

# m = max_index
# f = max_index + interval - 1 
# data = data2 = month[0]

# for x in range(len(count)):
#     if (max_index) > count[x]:
#         m = max_index - count[x]
#         data = month[x + 1]
#     if (max_index + interval) > count[x]:
#         data2 = month[x + 1]
#         f = (max_index + interval - 1) - count[x]

# print(f"Самый жаркий период: {m} {data} - {f} {data2} с температурой {long_wet[max_index:max_index+interval]}")