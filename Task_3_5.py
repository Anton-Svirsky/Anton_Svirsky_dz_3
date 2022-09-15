# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input("Enter k: "))

fibonacci_list = [0] * (k * 2 + 1)
fibonacci_list[k] = 0
fibonacci_list[k + 1] = 1

for i in range(k+2, len(fibonacci_list)):
    fibonacci_list[i] = fibonacci_list[i - 2] + fibonacci_list[i - 1]
for i in range(k, -1, -1):
    fibonacci_list[i] = fibonacci_list[i + 2] - fibonacci_list[i + 1]
print(fibonacci_list)
