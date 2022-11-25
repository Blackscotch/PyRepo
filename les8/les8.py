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

groups = ['Первая', 'Вторая', 'Третья', 'Четвертая']
groups_table = CreateGroups(groups)
print(BestResult(groups_table))
print()

input("Нажмите что-нибудь для выполнения след. задачи: ")
os.system("cls")

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

matrix = CreateMatrix(int(input("Введите размер матрицы: ")))
print(SumMatrix(matrix))

print()

input("Нажмите что-нибудь для выполнения след. задачи: ")
os.system("cls")

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
        print(f"{wether[i]} - {month[i]}")
    return wether

# Транформируем все в один список и возвращаем
def TransforWether(wether):
    days = []
    for month in wether:
        for items in month:
            days.append(items)
    return days

# Находим индексы последнего дня каждого месяца
def FindMothLen(wether):
    count_days = []
    summa = 0
    for month in wether:
        summa += len(month)
        count_days.append(summa - 1)
    return count_days
    
# Находим индексы максимально высокой и максимально низкой температуры и возвращаем
def FindMinMaxIndex(days, interval):
    min = max = sum(days[0:interval])
    min_index = 0
    max_index = 0
    for i in range(len(days) - interval + 1):
        if max < sum(days[i:i+interval]):
            max = sum(days[i:i+interval])
            max_index = i
        if min > sum(days[i:i+interval]):
            min = sum(days[i:i+interval])
            min_index = i
    return [max_index, min_index]

def ShowIntervals(month, days, count_days, interval, index_temp):
    date_max = date2_max = date_min = date2_min = month[0]
    first_day_max = index_temp[0] + 1
    last_day_max = index_temp[0] + interval - 1
    first_day_min = index_temp[1] + 1
    last_day_min = index_temp[1] + interval - 1

    for x in range(len(count_days)):
        if index_temp[0] > count_days[x]:
            first_day_max = index_temp[0] - count_days[x]
            date_max = month[x + 1]
        if (index_temp[0] + interval) > count_days[x]:
            last_day_max = (index_temp[0] + interval - 1) - count_days[x]
            date2_max = month[x + 1]
        if index_temp[1] > count_days[x]:
            first_day_min = index_temp[1] - count_days[x]
            date_min = month[x + 1]
        if (index_temp[1] + interval) > count_days[x]:
            last_day_min = (index_temp[1] + interval - 1) - count_days[x]
            date2_min = month[x + 1]
    print(f"Самый жаркий период ({interval} дня): {first_day_max} {date_max} - {last_day_max} {date2_max} с температурой {days[index_temp[0]:index_temp[0] + interval]}")
    print(f"Самый холодный период ({interval} дня): {first_day_min} {date_min} - {last_day_min} {date2_min} с температурой {days[index_temp[1]:index_temp[1] + interval]}")

month = ['Май', 'Июнь', 'Июль', 'Август', 'Сентябрь']
wether = CreateWether(month)
days = TransforWether(wether)
count_days = FindMothLen(wether)
interval = int(input("Введите интервал: "))
index_temp = FindMinMaxIndex(days, interval)
ShowIntervals(month, days, count_days, interval, index_temp)