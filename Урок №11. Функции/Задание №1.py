def factorial(n):
    """Функция для вычисления факториала числа n"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# 1. Ввод числа
num = int(input("Введите натуральное число: "))

# 2. Находим факториал введенного числа
first_factorial = factorial(num)
print(f"Факториал числа {num} равен {first_factorial}")

# 3. Создаем список факториалов от first_factorial до 1 в убывающем порядке
result_list = []
for i in range(first_factorial, 0, -1):
    result_list.append(factorial(i))

# 4. Вывод результата
print("Результирующий список:")
print(result_list)

input("\nНажмите Enter, чтобы выйти...")
