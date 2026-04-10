numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
seen = set()

print("Результат проверки:")
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num) # Добавляем новое число в историю

input("\nНажмите Enter, чтобы выйти...")
