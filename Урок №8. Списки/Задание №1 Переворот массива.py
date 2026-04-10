n = int(input("Введите кол-во чисел (N): "))
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

print("Результат:", *(numbers[::-1]))
input("\nНажмите Enter для выхода...")
