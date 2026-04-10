pets = {}

# Сбор данных
name = input("Введите имя питомца: ")
type_pet = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя владельца: ")

# Добавляем данные в словарь
pets[name] = {
    "Вид питомца": type_pet,
    "Возраст питомца": age,
    "Имя владельца": owner
}

# Логика для правильного склонения слова "год"
if age % 10 == 1 and age % 100 != 11:
    year_string = "год"
elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
    year_string = "года"
else:
    year_string = "лет"

# Извлекаем данные через методы keys() и values() для вывода
# Нам нужно имя (ключ) и характеристики (значения внутреннего словаря)
pet_name = list(pets.keys())[0]
pet_info = list(pets[pet_name].values())

# Формируем итоговую строку
print(f'Это {pet_info[0]} по кличке "{pet_name}". '
      f'Возраст питомца: {pet_info[1]} {year_string}. '
      f'Имя владельца: {pet_info[2]}')

input("\nНажмите Enter, чтобы выйти...")
