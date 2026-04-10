m = int(input("Введите макс. вес лодки (M): "))
n = int(input("Введите кол-во рыбаков (N): "))
weights = []
for i in range(n):
    w = int(input(f"Введите вес рыбака {i+1}: "))
    weights.append(w)

weights.sort()

left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boats += 1

print(f"Нужно лодок: {boats}")
input("\nНажмите Enter для выхода...")
