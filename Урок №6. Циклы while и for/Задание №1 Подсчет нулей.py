n = int(input("Введите количество чисел: "))
count_zeros = 0
for i in range(n):
    if int(input(f"Число {i+1}: ")) == 0:
        count_zeros += 1
print("Количество нулей:", count_zeros)

input("\nНажмите Enter, чтобы выйти...")
