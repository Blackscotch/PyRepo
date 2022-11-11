import random
# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
size = 10
numbers = [random.randint(1, 10) for _ in range(size)]
# numbers = [4, 1, 5, 2, 3, 4, 6, 1, 7, 8]
size = len(numbers)
print(numbers) 
mew_list = []
first = numbers[0]
set = []
for x in range(1, size):
    if first < numbers[x]:
        set.append(first)
        if x == size - 1:
            set.append(numbers[x])
            mew_list.append(set)
    else:
        if len(set) != 0:
          set.append(first)
          mew_list.append(set)
          set = []
    first = numbers[x]
print(str(mew_list).replace("],", "] или"))    