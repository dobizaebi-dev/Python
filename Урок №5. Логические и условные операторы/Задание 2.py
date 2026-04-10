word = input("Введите слово: ").lower()
vowels_list = ['a', 'e', 'i', 'o', 'u']

vowels_count = 0
consonants_count = 0
vowels_dict = {v: 0 for v in vowels_list}

for letter in word:
    if letter in vowels_list:
        vowels_count += 1
        vowels_dict[letter] += 1
    elif letter.isalpha():
        consonants_count += 1

print(f"Гласных: {vowels_count}, согласных: {consonants_count}")

for v in vowels_list:
    if vowels_dict[v] > 0:
        print(f"Буква '{v}': {vowels_dict[v]}")
    else:
        print(f"Буква '{v}': False")
