class Cassa:
    def __init__(self, amount=0):
        # Текущее количество денег в кассе
        self.money = amount

    def top_up(self, X):
        # Пополнить кассу на X
        self.money += X
        print(f"Пополнение на {X}. В кассе: {self.money}")

    def count_1000(self):
        # Сколько целых тысяч в кассе (используем целочисленное деление)
        thousands = self.money // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands

    def take_away(self, X):
        # Забрать деньги или выдать ошибку
        if X <= self.money:
            self.money -= X
            print(f"Выдано {X}. Остаток в кассе: {self.money}")
        else:
            print(f"Ошибка: недостаточно денег! (В наличии только {self.money})")

# Проверка работы
my_cassa = Cassa(500)
my_cassa.top_up(1700)      # Баланс 2200
my_cassa.count_1000()      # Выведет 2
my_cassa.take_away(3000)   # Ошибка
my_cassa.take_away(1000)   # Баланс 1200

# Чтобы консоль не закрывалась
input("\nНажмите Enter для выхода...")
