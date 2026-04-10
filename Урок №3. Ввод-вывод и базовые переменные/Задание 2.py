# Список правильных ответов для сверки
correct_stages = [
    "Дриопитек",
    "Австралопитек",
    "Человек умелый",
    "Человек прямоходящий",
    "Неандерталец",
    "Кроманьонец",
    "Homo sapiens sapiens"
]

user_answers = []
score = 0

print("--- Тест по биологии: Этапы развития человека ---")

# Цикл для запроса всех 7 этапов
for i in range(len(correct_stages)):
    answer = input(f"Введите {i+1}-й этап развития: ")
    user_answers.append(answer)
    
    # Сравниваем ответ (приводим к нижнему регистру для гибкости)
    if answer.lower() == correct_stages[i].lower():
        score += 1
        print("Верно!")
    else:
        print(f"Ошибка. Правильно: {correct_stages[i]}")

print("\n--- Результаты ---")
# Выводим цепочку через разделитель => как в задании
print("Ваша цепочка:", *user_answers, sep=" => ")

# Итоговый балл
print(f"Правильных ответов: {score} из {len(correct_stages)}")

# Чтобы консоль не закрылась
input("\nНажмите Enter, чтобы выйти...")
