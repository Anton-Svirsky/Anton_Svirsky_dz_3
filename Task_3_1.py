# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import *
new_list = [randint(0, 10) for _ in range(0, 5)]
_sum = 0
for i in range(0, 5):
    if i % 2 != 0:
        _sum = _sum + new_list[i]
print(f'{new_list} ответ: {_sum}')
