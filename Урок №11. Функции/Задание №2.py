import collections
import json
import os

DB_FILE = "pets_db.json"

def save_db():
    with open(DB_FILE, "w", encoding="utf-8") as f:
        # Преобразуем ключи в строки для JSON, так как он не принимает инты как ключи
        json.dump(pets, f, ensure_ascii=False, indent=4)

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # Важно: превращаем строковые ключи обратно в числа
                return {int(k): v for k, v in data.items()}
            except:
                return {}
    return {}

pets = load_db()

def get_pet(ID):
    return pets[ID] if ID in pets else False

def get_suffix(age):
    if 11 <= age % 100 <= 14: return 'лет'
    last_digit = age % 10
    if last_digit == 1: return 'год'
    if 2 <= last_digit <= 4: return 'года'
    return 'лет'

def create():
    if not pets:
        new_id = 1
    else:
        # Самый надежный способ получить последний ID без deque:
        new_id = max(pets.keys()) + 1
    
    name = input("Введите кличку: ")
    kind = input("Вид питомца: ")
    
    # Чтобы не вылетало на вводе возраста:
    try:
        age = int(input("Возраст питомца: "))
    except ValueError:
        print("Ошибка! Возраст должен быть числом. Установлено: 0")
        age = 0
        
    owner = input("Имя владельца: ")
    
    # Создаем структуру как в задании
    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    
    # Пробуем сохранить. Если вылетает здесь — значит, среде запрещено создавать файлы
    try:
        save_db()
    except Exception as e:
        print(f"Предупреждение: Не удалось сохранить файл ({e})")
        
    print(f"Запись успешно добавлена под ID: {new_id}")

def read():
    try:
        ID = int(input("Введите ID: "))
        pet_data = get_pet(ID)
        if pet_data:
            name = list(pet_data.keys())[0]
            details = pet_data[name]
            age = details["Возраст питомца"]
            print(f'Это {details["Вид питомца"]} по кличке "{name}". '
                  f'Возраст питомца: {age} {get_suffix(age)}. Имя владельца: {details["Имя владельца"]}')
        else:
            print("ID не найден.")
    except ValueError:
        print("Введите число.")

def update():
    try:
        ID = int(input("Введите ID для обновления: "))
        pet_data = get_pet(ID)
        if pet_data:
            old_name = list(pet_data.keys())[0]
            new_name = input(f"Новая кличка (Enter, чтобы оставить '{old_name}'): ") or old_name
            new_kind = input("Новый вид: ")
            new_age = int(input("Новый возраст: "))
            new_owner = input("Новый владелец: ")
            pets[ID] = {new_name: {"Вид питомца": new_kind, "Возраст питомца": new_age, "Имя владельца": new_owner}}
            save_db()
            print("Данные обновлены.")
        else:
            print("ID не найден.")
    except ValueError:
        print("Ошибка ввода.")

def delete():
    try:
        ID = int(input("Введите ID для удаления: "))
        if ID in pets:
            del pets[ID]
            save_db()
            print(f"Запись {ID} удалена.")
        else:
            print("ID не найден.")
    except ValueError:
        print("Введите число.")

def pets_list():
    if not pets:
        print("База пуста.")
        return
    for pet_id, data in pets.items():
        name = list(data.keys())[0]
        print(f"ID: {pet_id} | Кличка: {name}")

command = ''
while command != 'stop':
    print("\nКоманды: create, read, update, delete, list, stop")
    command = input("Введите команду: ").strip().lower()
    
    if command == 'create': create()
    elif command == 'read': read()
    elif command == 'update': update()
    elif command == 'delete': delete()
    elif command == 'list': pets_list()
    elif command == 'stop': print("Программа завершена.")
