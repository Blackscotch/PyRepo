import random
from collections import Counter

# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8
numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)
numbers = list(filter(lambda x: x > 5, numbers))
print(numbers)


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
size = 10
numbers = [random.randint(1, 10) for _ in range(size)]
print(numbers)
index = random.randint(0, size - 1)
result = [numbers[index]]

while index < size:
    index = random.randint(index+1, size)
    if index < size:
        if numbers[index] > result[-1]:
            result.append(numbers[index])
print(result)


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают.Список уникальных элементов
# [1, 4, 2, 3, 6, 7]
numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)
print(f"Совпадающих элементов: {sum(list(filter(lambda x: x > 1, Counter(numbers).values())))}")
print(f"Список уникальных элементов {Counter(numbers).keys()}")
