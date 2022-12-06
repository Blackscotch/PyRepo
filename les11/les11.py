import matplotlib.pyplot as plt
from random import randint
from pathlib import Path
import csv

# Задача 1. Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.

x = [x for x in range(-10, 10)]
y = [5 * i**2 + 10 * i - 30 for i in x ]
x_line = []
y_line = []
for i in range(len(y)):
    if y[i] < 0:
        x_line.append(x[i])
        y_line.append(y[i])  
plt.plot(x, y)
plt.plot(x_line, y_line)   
plt.ylabel('Ось Y')
plt.xlabel('Ось X')
plt.show()

print()
input("Для выполнения следующей задачи нажмите что-нибудь: ")



# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
def Result():
    finish_list = []
    for i in range(lenth):
        if meter_coast[i] < limit_price:
            finish_list.append((houses[i], hous_area[i], hous_price[i], meter_coast[i]))
    return finish_list

def WriteResult(data):
    path = Path("les11", "res.csv")
    with open(path, 'w', encoding='utf-8') as file:
        for line in data:
            file.write('Дом №: {};Площадь: {};Стоимость дома: {};Стоимость кв.м. {}\n'.format(line[0], line[1], line[2], line[3]))

houses = [x for x in range(1, 16)]
lenth = len(houses)
hous_area = [randint(100, 300) for _ in range(lenth)]
hous_price = [randint(3000000, 20000000) for _ in range(lenth)]
limit_price = 50000
limit_price_line = [limit_price for _ in range(lenth)]
meter_coast = [int(hous_price[i]/hous_area[i]) for i in range(lenth)]


final = Result()
print(final)
final.sort(key=lambda x: x[1])
print(final)
WriteResult(final)

plt.bar(houses, meter_coast)
plt.plot(houses, limit_price_line, 'y')   
plt.ylabel('Стоимость за кв. метр')   
plt.xlabel('Дома') 
plt.show()