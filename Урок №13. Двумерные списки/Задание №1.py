import random

def create_matrix_random(rows, cols):
    """Генерирует матрицу со случайными числами"""
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

def create_matrix_manual(rows, cols, name):
    """Позволяет пользователю ввести каждое число вручную"""
    print(f"\nЗаполнение матрицы {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    val = int(input(f"Введите элемент [{i+1}][{j+1}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Ошибка! Введите целое число.")
        matrix.append(row)
    return matrix

def add_matrices(m1, m2):
    """Складывает две матрицы"""
    rows = len(m1)
    cols = len(m1[0])
    return [[m1[i][j] + m2[i][j] for j in range(cols)] for i in range(rows)]

def print_matrix(matrix, title):
    """Красивый вывод матрицы"""
    print(f"\n--- {title} ---")
    for row in matrix:
        print(" ".join(f"{num:5}" for num in row))

# --- Основной код ---

try:
    # 1. Задание размеров
    r = int(input("Введите количество строк: "))
    c = int(input("Введите количество столбцов: "))

    # 2. Выбор способа заполнения
    print("\nКак заполнить матрицы?")
    print("1 - Случайными числами")
    print("2 - Вручную")
    choice = input("Ваш выбор (1 или 2): ")

    if choice == '1':
        matrix_1 = create_matrix_random(r, c)
        matrix_2 = create_matrix_random(r, c)
    else:
        matrix_1 = create_matrix_manual(r, c, "№1")
        matrix_2 = create_matrix_manual(r, c, "№2")

    # 3. Сложение и вывод
    matrix_3 = add_matrices(matrix_1, matrix_2)

    print_matrix(matrix_1, "Матрица 1")
    print_matrix(matrix_2, "Матрица 2")
    print_matrix(matrix_3, "Результат сложения")

except ValueError:
    print("\nОшибка: нужно было вводить целые числа для размеров!")

# Защита от вылета
print("\n" + "="*30)
input("Нажмите Enter для выхода...")