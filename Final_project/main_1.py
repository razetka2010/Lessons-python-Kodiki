#TODO: Подключение библеотек
import random
import json

#TODO: подключаем texts.json к проекту
with open("texts.json", "r", encoding="utf-8") as f:
    texts = json.load(f)

#TODO: объединяем все тексты
all_texts = ""
for key in texts:
    all_texts = all_texts + " " + texts[key]

#TODO: разбиваем текст на слова
words = all_texts.lower().split()

model = {}

#TODO: обучение модели
for i in range(len(words) - 1):
    current_word = words[i] # берём текущее слово
    next_word = words[i + 1] # берём следущее слово

    if current_word not in model: # проверка слова в модели
        model[current_word] = [] # "запихиваем" слово в массив

    model[current_word].append(next_word) # добавление следуещего слова в массив

print("ИИ обучен")
print("Количество слов в модели:", len(model))

current_word = random.choice(words)
result = [current_word]

#TODO: сколько слов сгенерировать
try:
    length = int(input("Сколько слов сгенерировать? "))
except:
    print("Введи число! Поставлю 20 слов.")
    length = 20

#TODO: генерируем текст
for j in range(length):
    next_words = model.get(current_word) # проврка следующего слова

    # остановка ии если нет списка
    if not next_words:
        break

    # выбор и вывод следующего слова
    current_word = random.choice(next_words)
    result.append(current_word)

generated_text = " ".join(result) # все слова через пробел в одну строку

print("\nСгенерированный текст:")
print(generated_text)