from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Здравствуй",
    "Привет",
    "Как дела?",
    "Что ты умеешь?",
    "Пока",
    "До свидания",
    "Пог",
    "Если пог погу не пог то пог не пог",
    "Замечательно",
    "Хорошо",
    "Какая погода?",
    "Идет дождь",
    "Ты классный",
    "молодец"
]

labels = [
    "Приветствие",
    "Приветствие",
    "Вопрос",
    "Вопрос",
    "Прощание",
    "Прощание",
    "Шутка",
    "Шутка",
    "Настроение",
    "Настроение",
    "Погода",
    "Погода",
    "Комплимент",
    "Комплимент"
]

answers = {
    "Приветствие": "Привет!",
    "Вопрос": "Нормально",
    "Прощание": "Пока",
    "Шутка": "Пог",
    "Настроение": "ну и хорошо",
    "Погода": "хз",
    "Комплимент": "Спасибо"
}

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

print("ИИ готов общаться!")

while True:
    text = input("Ты: ")
    if text.lower() == "выход":
        print("ИИ: Пока!")
        break

    X_test = vectorizer.transform([text])
    result = model.predict(X_test)[0]
    
    print(f"ИИ думает что это - {result}: {answers.get(result, 'Я пока не знаю, что мне ответить')}")
