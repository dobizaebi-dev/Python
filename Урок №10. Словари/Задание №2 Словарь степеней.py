import random

my_dict = {}

# Проходим по диапазону от 10 до -5 включительно
for i in range(10, -6, -1):
    # Генерируем случайное число для возведения в степень (например, от 2 до 5)
    random_base = random.randint(2, 5)
    
    # Ключ — число из диапазона, значение — случайное число в степени этого ключа
    try:
        my_dict[i] = random_base ** i
    except ZeroDivisionError:
        my_dict[i] = 0

# Выводим результат
print("Рандомизированный словарь (ключи от 10 до -5):")
for key, value in my_dict.items():
    # Если число очень маленькое (дробное), выводим 5 знаков после запятой
    if isinstance(value, float):
        print(f"{key}: {value:.5f}")
    else:
        print(f"{key}: {value}")

input("\nНажмите Enter, чтобы выйти...")
