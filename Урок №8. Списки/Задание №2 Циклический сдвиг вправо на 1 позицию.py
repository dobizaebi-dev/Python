n = int(input("Введите кол-во чисел (N): "))
a = list(map(int, input("Введите числа через пробел: ").split()))

if len(a) > 1:
    a = [a[-1]] + a[:-1]

print("Результат:", *a)
input("\nНажмите Enter для выхода...")
