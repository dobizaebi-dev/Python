x = int(input("Минимальная сумма (X): "))
a = int(input("Деньги Майкла (A): "))
b = int(input("Деньги Ивана (B): "))

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)
