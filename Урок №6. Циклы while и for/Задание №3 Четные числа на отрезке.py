a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a % 2 != 0:
    a += 1

print("Четные числа:")
for i in range(a, b + 1, 2):
    print(i, end=' ')

input("\n\nНажмите Enter, чтобы выйти...")
