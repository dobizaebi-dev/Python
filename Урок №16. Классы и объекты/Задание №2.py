import math

class Черепашка:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        # В условии было сказано y, но для движения вправо меняем x
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            print("Ошибка: s не может быть меньше или равно 0!")
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        # Считаем расстояние по горизонтали и вертикали
        target_x = abs(x2 - self.x)
        target_y = abs(y2 - self.y)
        
        # Минимальное кол-во ходов — это расстояние, деленное на шаг s, 
        # округленное в большую сторону
        moves_x = math.ceil(target_x / self.s)
        moves_y = math.ceil(target_y / self.s)
        
        return moves_x + moves_y

# --- Пример использования ---
t = Черепашка(0, 0, 2)
t.go_up()      # y станет 2
t.go_right()   # x станет 2
t.evolve()     # s станет 3

print(f"Позиция: ({t.x}, {t.y}), Шаг: {t.s}")
print(f"Минимум действий до (10, 10): {t.count_moves(10, 10)}")

# Чтобы консоль не закрывалась
input("\nНажмите Enter для выхода...")
