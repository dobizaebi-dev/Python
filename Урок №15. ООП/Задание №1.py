# Задание №1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def display_info(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

bus_1 = Autobus("Renaul Logan", 180, 12)
bus_1.display_info()


# Задание №2
class Transport2: # Переименовал, чтобы не было конфликта в одном файле
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

class Autobus2(Transport2):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

bus_2 = Autobus2("Renaul Logan", 180, 12)
print(bus_2.seating_capacity())

# ЭТА СТРОЧКА ОСТАНОВИТ ВЫЛЕТ:
input("\nНажмите Enter, чтобы выйти...")
