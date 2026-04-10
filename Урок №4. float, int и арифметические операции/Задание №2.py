try:
    num = int(input("Введите пятизначное целое число: "))
    
    # Проверка на пятизначность
    if 10000 <= abs(num) <= 99999:
        # Извлекаем цифры
        ones = abs(num) % 10                # Единицы
        tens = (abs(num) // 10) % 10        # Десятки
        hundreds = (abs(num) // 100) % 10   # Сотни
        thousands = (abs(num) // 1000) % 10 # Тысячи
        ten_thous = abs(num) // 10000       # Десятки тысяч

        # Алгоритм: (десятки ^ единицы) * сотни / (десятки_тысяч - тысячи)
        # Используем float() для получения вещественного числа
        denominator = ten_thous - thousands
        
        if denominator == 0:
            print("Ошибка: Деление на ноль (разность первой и второй цифры равна 0)")
        else:
            result = float((tens ** ones) * hundreds / denominator)
            print(f"Результат вычислений: {result}")
    else:
        print("Ошибка: Число должно быть пятизначным (от 10000 до 99999)!")

except ValueError:
    print("Ошибка: Введите целое число!")

input("\nНажмите Enter, чтобы выйти...")