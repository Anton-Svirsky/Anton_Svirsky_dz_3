# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import *
new_list = [randint(0, 10) for _ in range(randint(4, 10))]
if len(new_list) % 2 != 0:
    print('The number of elements in the list is not even!')
    temp = int(len(new_list) / 2) + 1
else:
    temp = int(len(new_list) / 2)
mult = []
for i in range(0, temp):
    mult.append(new_list[i] * new_list[len(new_list) - 1 - i])
print(f'{new_list} -> {mult}')
